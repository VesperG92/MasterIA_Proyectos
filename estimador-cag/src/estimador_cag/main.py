from fastapi import FastAPI
from estimador_cag.routers import estimations

app = FastAPI(
    title="Estimador CAG",
    description="Sistema de estimación de software con arquitectura CAG",
    version="0.1.0"
)

app.include_router(estimations.router)

@app.get("/health")
async def health():
    return {"status": "healthy"}