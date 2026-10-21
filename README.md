# MasterIA_Proyectos
Projects repository from IA Masters

## Arrancar el servidor
uv run uvicorn estimador_cag.main:app --reload

http://localhost:8000/docs#/estimations/estimate_api_v1_estimate_post

## Ejemplo body para el POST
{
  "transcription": "En la reunión con el cliente se discutió la necesidad de una aplicación móvil con login, catálogo de productos, carrito de compra y pasarela de pago. El cliente quiere tenerlo listo en tres meses."
}

## Testing con pytest
Desde la carpeta de proyecto estimador-cag
- uv add --dev pytest httpx ruff
- uv run pytest -v 
