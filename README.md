# MasterIA_Proyectos
Projects repository

## Arrancar el servidor
uv run uvicorn estimador_cag.main:app --reload

http://localhost:8000/docs#/estimations/estimate_api_v1_estimate_post

## Ejemplo body para el POST
{
  "transcription": "En la reunión con el cliente se discutió la necesidad de una aplicación móvil con login, catálogo de productos, carrito de compra y pasarela de pago. El cliente quiere tenerlo listo en tres meses."
}