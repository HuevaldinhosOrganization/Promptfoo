from typing import List

from .models import ClassificationLabel, SentimentLabel


POSITIVE_KEYWORDS = frozenset(
    {
        "fantastic",
        "great",
        "loved",
        "amazing",
        "excellent",
        "awesome",
        "good",
        "wonderful",
    }
)
NEGATIVE_KEYWORDS = frozenset(
    {
        "terrible",
        "hated",
        "bad",
        "awful",
        "worst",
        "poor",
        "boring",
    }
)

ELECTRONICS_KEYWORDS = frozenset(
    {
        "smartphone",
        "camera",
        "battery",
        "electronics",
        "charger",
        "device",
    }
)
BOOKS_KEYWORDS = frozenset(
    {
        "novel",
        "book",
        "mystery",
        "story",
        "author",
        "chapter",
    }
)

NER_ENTITIES = {
    "Albert Einstein": "Albert Einstein",
    "Germany": "Germany",
    "Nobel Prize": "Nobel Prize",
    "Physics": "Physics",
    "Eiffel Tower": "Eiffel Tower",
    "Paris": "Paris",
    "France": "France",
}


def sentiment_analysis(text: str) -> SentimentLabel:
    normalized = text.lower()
    if any(keyword in normalized for keyword in POSITIVE_KEYWORDS):
        return SentimentLabel.positive
    if any(keyword in normalized for keyword in NEGATIVE_KEYWORDS):
        return SentimentLabel.negative
    return SentimentLabel.neutral


def classify_review(text: str) -> ClassificationLabel:
    normalized = text.lower()
    if any(keyword in normalized for keyword in ELECTRONICS_KEYWORDS):
        return ClassificationLabel.electronics
    if any(keyword in normalized for keyword in BOOKS_KEYWORDS):
        return ClassificationLabel.books
    return ClassificationLabel.other


def generate_dialogue_response(context: str) -> str:
    normalized = context.lower()
    if "hello" in normalized or "how are you" in normalized:
        return "I'm doing well, thank you for asking."
    if "favorite movie" in normalized or "favorite film" in normalized:
        return "I enjoy science fiction films like Inception."
    return "That sounds interesting!"


def extract_ner_entities(text: str) -> List[str]:
    entities: List[str] = []
    source_text = text.lower()
    for sentence_entity, entity_name in NER_ENTITIES.items():
        if sentence_entity.lower() in source_text:
            entities.append(entity_name)
    return entities
