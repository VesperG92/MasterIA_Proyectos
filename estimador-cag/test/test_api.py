from fastapi.testclient import TestClient

from estimador_cag.main import app

client = TestClient(app)

VALID_TEXT = (
    "En la reunión con el cliente se discutió la necesidad de una aplicación "
    "móvil con login, catálogo de productos y pasarela de pago."
)


def test_health():
    assert client.get("/health").status_code == 200


def test_openapi_exposes_estimate():
    paths = client.get("/openapi.json").json()["paths"]
    assert "/api/v1/estimate" in paths


def test_estimate_ok(monkeypatch):
    async def fake_generate(transcription: str) -> dict:
        return {
            "estimation": "## Estimación: prueba",
            "model": "claude-test-model",
            "provider": "anthropic",
            "tokens_used": 10,
        }

    monkeypatch.setattr("estimador_cag.routers.estimations.generate_estimation", fake_generate)

    response = client.post("/api/v1/estimate", json={"transcription": VALID_TEXT})

    assert response.status_code == 200
    body = response.json()
    assert body["estimation"].startswith("## Estimación")
    assert body["provider"] == "anthropic"


def test_estimate_missing_field_returns_422():
    assert client.post("/api/v1/estimate", json={}).status_code == 422


def test_estimate_too_short_returns_422():
    response = client.post("/api/v1/estimate", json={"transcription": "hola"})
    assert response.status_code == 422


def test_estimate_llm_failure_returns_502(monkeypatch):
    async def failing_generate(transcription: str) -> dict:
        raise RuntimeError("fallo simulado")

    monkeypatch.setattr("estimador_cag.routers.estimations.generate_estimation", failing_generate)

    response = client.post("/api/v1/estimate", json={"transcription": VALID_TEXT})

    assert response.status_code == 502
    assert "fallo simulado" in response.json()["detail"]