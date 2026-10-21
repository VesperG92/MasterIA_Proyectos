# routers/estimations.py
# gestiona la comunicación HTTP
import anthropic
from fastapi import APIRouter, HTTPException

from estimador_cag.schemas.estimation import EstimationRequest, EstimationResponse
from estimador_cag.services.llm_service import generate_estimation

router = APIRouter(prefix="/api/v1", tags=["estimations"])

@router.post("/estimate", response_model=EstimationResponse)
async def estimate(request: EstimationRequest):
    try:
        result = await generate_estimation(request.transcription)
    except anthropic.APIError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Error al generar la estimación: {exc}",
        ) from exc
    return result
