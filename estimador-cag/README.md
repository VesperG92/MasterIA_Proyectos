## Arquitectura y flujo del estimador

Esta sección describe cómo viaja una petición desde que llega a la API hasta que se devuelve la respuesta.

```text
Cliente (curl, Swagger, app frontend)
    │  1. Petición HTTP
    ▼
main.py
    │  2. Enruta la petición
    ▼
routers/estimations.py
    │  3. Valida el request con Pydantic
    ▼
services/llm_service.py
    │  4. Construye el prompt con el contexto de context/
    ▼
API del LLM (OpenAI / Anthropic)
    │  5. Genera la respuesta
    ▼
services/llm_service.py
    │  6. Procesa la respuesta del LLM
    ▼
routers/estimations.py
    │  7. Serializa el response con Pydantic
    ▼
Cliente (respuesta JSON)
```

### Paso a paso

| # | Componente | Responsabilidad |
|---|------------|-----------------|
| 1 | **Cliente** | Envía la petición (curl, Swagger UI o una app frontend). |
| 2 | `main.py` | Punto de entrada de la aplicación; redirige la petición al router correspondiente. |
| 3 | `routers/estimations.py` | Valida el cuerpo de la petición con modelos Pydantic. |
| 4 | `services/llm_service.py` | Construye el prompt incorporando el contexto almacenado en `context/`. |
| 5 | **API del LLM** | OpenAI o Anthropic generan la respuesta a partir del prompt. |
| 6 | `services/llm_service.py` | Procesa y normaliza la respuesta recibida del LLM. |
| 7 | `routers/estimations.py` | Serializa el resultado con Pydantic y lo devuelve como JSON. |

### Separación de responsabilidades

- **Routers**: capa HTTP. Validación de entrada y serialización de salida.
- **Services**: lógica de negocio y comunicación con el LLM.
- **Context**: material de contexto que se inyecta en los prompts.