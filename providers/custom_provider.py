from typing import Any, Dict, Optional

POSITIVE_KEYWORDS = {
    "fantastic",
    "great",
    "loved",
    "amazing",
    "excellent",
    "awesome",
    "good",
    "wonderful",
}
NEGATIVE_KEYWORDS = {
    "terrible",
    "hated",
    "bad",
    "awful",
    "worst",
    "poor",
    "boring",
}

ELECTRONICS_KEYWORDS = {
    "smartphone",
    "camera",
    "battery",
    "electronics",
    "charger",
    "device",
}
BOOKS_KEYWORDS = {
    "novel",
    "book",
    "mystery",
    "story",
    "author",
    "chapter",
}

NER_ENTITIES = {
    "Albert Einstein": "Albert Einstein",
    "Germany": "Germany",
    "Nobel Prize": "Nobel Prize",
    "Physics": "Physics",
    "Eiffel Tower": "Eiffel Tower",
    "Paris": "Paris",
    "France": "France",
}


def sentiment_analysis(text: str) -> str:
    normalized = text.lower()
    if any(keyword in normalized for keyword in POSITIVE_KEYWORDS):
        return "positive"
    if any(keyword in normalized for keyword in NEGATIVE_KEYWORDS):
        return "negative"
    return "neutral"


def classify_review(text: str) -> str:
    normalized = text.lower()
    if any(keyword in normalized for keyword in ELECTRONICS_KEYWORDS):
        return "electronics"
    if any(keyword in normalized for keyword in BOOKS_KEYWORDS):
        return "books"
    return "other"


def generate_dialogue_response(context: str) -> str:
    normalized = context.lower()
    if "hello" in normalized or "how are you" in normalized:
        return "I'm doing well, thank you for asking."
    if "favorite movie" in normalized or "favorite film" in normalized:
        return "I enjoy science fiction films like Inception."
    return "That sounds interesting!"


def extract_ner_entities(text: str) -> list[str]:
    normalized = text.lower()
    entities = [value for key, value in NER_ENTITIES.items() if key.lower() in normalized]
    return entities


def call_api(prompt: str, options: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    task = (context or {}).get("vars", {}).get("task", "sentiment")
    vars_map = (context or {}).get("vars", {})

    if task == "sentiment":
        result = sentiment_analysis(vars_map.get("text", ""))
    elif task == "classify":
        result = classify_review(vars_map.get("text", ""))
    elif task == "dialogue":
        result = generate_dialogue_response(vars_map.get("context", ""))
    elif task == "ner":
        result = ", ".join(extract_ner_entities(vars_map.get("text", ""))) or ""
    else:
        return {"error": f"Unsupported task: {task}"}

    return {"output": result}
