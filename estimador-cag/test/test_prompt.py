from estimador_cag.context.examples import ESTIMATION_EXAMPLES
from estimador_cag.services.llm_service import build_system_prompt


def test_examples_have_expected_keys():
    assert len(ESTIMATION_EXAMPLES) > 0
    for ex in ESTIMATION_EXAMPLES:
        assert "meeting_summary" in ex
        assert "estimation" in ex


def test_system_prompt_includes_examples():
    prompt = build_system_prompt()
    assert "Ejemplo 1" in prompt
    assert "experto en estimación" in prompt