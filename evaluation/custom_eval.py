from difflib import SequenceMatcher
from typing import Any, Dict, TypedDict


class EvalResult(TypedDict):
    pass_: bool
    score: float
    reason: str


def get_assert(output: str, context: Dict[str, Any]) -> EvalResult:
    expected = str(context["vars"].get("expected", "")).strip().lower()
    output_clean = output.strip().lower()

    if not output_clean:
        return {"pass_": False, "score": 0.0, "reason": "Output is empty"}

    if expected in ["positive", "negative"]:
        return _assert_exact(output_clean, expected, "sentiment")

    if expected in ["electronics", "books"]:
        return _assert_exact(output_clean, expected, "classification")

    if "," in expected:
        return _assert_entities(output_clean, expected)

    return _assert_similarity(output_clean, expected)


def _assert_exact(output_clean: str, expected: str, category: str) -> EvalResult:
    if output_clean == expected:
        return {"pass_": True, "score": 1.0, "reason": f"Correct {category}: {expected}"}
    return {
        "pass_": False,
        "score": 0.0,
        "reason": f"Incorrect {category}, expected {expected}, got {output_clean}",
    }


def _assert_entities(output_clean: str, expected: str) -> EvalResult:
    expected_entities = {e.strip() for e in expected.split(",") if e.strip()}
    output_entities = {e.strip() for e in output_clean.split(",") if e.strip()}

    if expected_entities.issubset(output_entities):
        score = len(expected_entities.intersection(output_entities)) / len(expected_entities)
        return {"pass_": True, "score": score, "reason": f"Entities matched ({score:.2f})"}

    missing = expected_entities - output_entities
    return {
        "pass_": False,
        "score": 0.0,
        "reason": f"Missing entities: {', '.join(sorted(missing))}",
    }


def _assert_similarity(output_clean: str, expected: str) -> EvalResult:
    similarity = SequenceMatcher(None, output_clean, expected).ratio()
    if similarity >= 0.6:
        return {"pass_": True, "score": similarity, "reason": f"Similarity {similarity:.2f}"}
    return {"pass_": False, "score": similarity, "reason": f"Low similarity ({similarity:.2f})"}
