from fastapi.testclient import TestClient

from backend.app import create_app

client = TestClient(create_app())


def test_sentiment_endpoint_positive():
    response = client.post("/sentiment", json={"text": "This movie was fantastic"})
    assert response.status_code == 200
    assert response.json() == {"result": "positive"}


def test_classify_endpoint_books():
    response = client.post("/classify", json={"text": "This novel is a thrilling mystery"})
    assert response.status_code == 200
    assert response.json() == {"result": "books"}


def test_dialogue_endpoint_returns_default_response():
    response = client.post("/dialogue", json={"context": "What's your favorite movie?"})
    assert response.status_code == 200
    assert response.json() == {"result": "I enjoy science fiction films like Inception."}


def test_ner_endpoint_returns_entities():
    response = client.post("/ner", json={"text": "The Eiffel Tower is located in Paris, France."})
    assert response.status_code == 200
    assert response.json() == {"result": "Eiffel Tower, Paris, France"}
