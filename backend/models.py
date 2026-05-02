from enum import Enum

from pydantic import BaseModel


class SentimentLabel(str, Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"


class ClassificationLabel(str, Enum):
    electronics = "electronics"
    books = "books"
    other = "other"


class SentimentRequest(BaseModel):
    text: str


class ClassifyRequest(BaseModel):
    text: str


class DialogueRequest(BaseModel):
    context: str


class NerRequest(BaseModel):
    text: str


class ResultResponse(BaseModel):
    result: str
