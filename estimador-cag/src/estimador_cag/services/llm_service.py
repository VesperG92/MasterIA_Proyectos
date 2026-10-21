# services/llm_service.py
from textwrap import dedent

from anthropic import AsyncAnthropic
from estimador_cag.config import get_settings
from estimador_cag.context.examples import ESTIMATION_EXAMPLES

settings = get_settings()
client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)


def format_examples(examples: list[dict]) -> str:
    bloques = []
    for i, ex in enumerate(examples, start=1):
        resumen = dedent(ex["meeting_summary"]).strip()
        estimacion = dedent(ex["estimation"]).strip()
        bloques.append(
            f"### Ejemplo {i}\n\n"
            f"**Resumen de la reunión:**\n{resumen}\n\n"
            f"**Estimación:**\n{estimacion}"
        )
    return "\n\n---\n\n".join(bloques)


def build_system_prompt() -> str:
    examples_text = format_examples(ESTIMATION_EXAMPLES)
    return f"""Eres un experto en estimación de proyectos de software.

Utiliza los siguientes presupuestos históricos como referencia:

{examples_text}

Genera una estimación detallada para el proyecto descrito.

Restricciones de longitud:
- La respuesta completa debe tener entre 1500 y 2000 palabras.
- Termina siempre con una conclusión completa; nunca dejes frases a medias.
- Si hay mucho contenido, prioriza lo esencial y resume el resto."""


async def generate_estimation(transcription: str) -> dict:
    system_prompt = build_system_prompt()

    response = await client.messages.create(
        model=settings.LLM_MODEL,
        max_tokens=4000,
        system=system_prompt,
        messages=[
            {"role": "user", "content": transcription},
        ],
    )
    print(repr(settings.LLM_MODEL), repr(settings.LLM_PROVIDER))
    return {
        "estimation": response.content[0].text,
        "model": settings.LLM_MODEL,
        "provider": settings.LLM_PROVIDER,
    }