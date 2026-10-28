from fastapi import FastAPI

from .routers import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Promptfoo NLP API",
        version="0.1.0",
        description="Reusable backend for NLP task evaluation and Promptfoo integration.",
    )
    app.include_router(router)
    return app


app = create_app()
