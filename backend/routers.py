from fastapi import APIRouter

from .models import (
    ClassifyRequest,
    DialogueRequest,
    NerRequest,
    ResultResponse,
    SentimentRequest,
)
from .services import (
    classify_review,
    extract_ner_entities,
    generate_dialogue_response,
    sentiment_analysis,
)

router = APIRouter()


@router.post("/sentiment", response_model=ResultResponse)
def sentiment_analysis_endpoint(req: SentimentRequest) -> ResultResponse:
    return ResultResponse(result=sentiment_analysis(req.text))


@router.post("/classify", response_model=ResultResponse)
def classify_review_endpoint(req: ClassifyRequest) -> ResultResponse:
    return ResultResponse(result=classify_review(req.text))


@router.post("/dialogue", response_model=ResultResponse)
def generate_dialogue_endpoint(req: DialogueRequest) -> ResultResponse:
    return ResultResponse(result=generate_dialogue_response(req.context))


@router.post("/ner", response_model=ResultResponse)
def extract_ner_endpoint(req: NerRequest) -> ResultResponse:
    return ResultResponse(result=", ".join(extract_ner_entities(req.text)) or "none")
