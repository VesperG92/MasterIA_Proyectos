from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "src" / "estimador_cag"

REQUIRED_FILES = [
    ROOT / "pyproject.toml",
    ROOT / "README.md",
    ROOT / ".env.example",
    PKG / "__init__.py",
    PKG / "main.py",
    PKG / "config.py",
    PKG / "routers" / "__init__.py",
    PKG / "routers" / "estimations.py",
    PKG / "schemas" / "__init__.py",
    PKG / "schemas" / "estimation.py",
    PKG / "services" / "__init__.py",
    PKG / "services" / "llm_service.py",
    PKG / "context" / "__init__.py",
    PKG / "context" / "examples.py",
]


@pytest.mark.parametrize("path", REQUIRED_FILES, ids=lambda p: str(p.relative_to(ROOT)))
def test_required_file_exists(path: Path):
    assert path.is_file(), f"Falta el archivo: {path.relative_to(ROOT)}"


def test_env_is_not_committed_example_exists():
    assert (ROOT / ".env.example").is_file()