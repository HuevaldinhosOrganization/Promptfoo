from backend.services import (
    classify_review,
    extract_ner_entities,
    generate_dialogue_response,
    sentiment_analysis,
)


def test_sentiment_analysis_positive():
    assert sentiment_analysis("This movie was fantastic and amazing") == "positive"


def test_sentiment_analysis_negative():
    assert sentiment_analysis("I hated this film, it was terrible") == "negative"


def test_classify_review_electronics():
    assert classify_review("This smartphone has a great camera") == "electronics"


def test_classify_review_books():
    assert classify_review("This novel has unexpected twists") == "books"


def test_generate_dialogue_response_greeting():
    assert generate_dialogue_response("Hello, how are you today?") == "I'm doing well, thank you for asking."


def test_extract_ner_entities():
    entities = extract_ner_entities("Albert Einstein won the Nobel Prize in Physics.")
    assert "Albert Einstein" in entities
    assert "Nobel Prize" in entities
    assert "Physics" in entities
