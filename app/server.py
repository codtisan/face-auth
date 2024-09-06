from fastapi import FastAPI
from datetime import datetime
from app.typings.healthcheck import HealthResponse
from app.typings.api_response import (
    FaceAuthResponse,
    FaceRegistrationResponse,
    FaceRegistrationResult,
    FaceAuthResult,
)

app = FastAPI()


@app.get("/")
async def get_health() -> HealthResponse:
    response = HealthResponse(
        status="success",
        status_code=200,
        message="OK!",
        timestamp=datetime.now(),
    )
    return response.model_dump()


@app.post("/register")
async def register() -> FaceRegistrationResponse:
    response = FaceRegistrationResponse(
        status="success",
        status_code=201,
        message="OK!",
        timestamp=datetime.now(),
        results=FaceRegistrationResult(success=True),
    )
    return response.model_dump()


@app.post("/auth")
async def authenticate() -> FaceAuthResponse:
    response = FaceAuthResponse(
        status="success",
        status_code=201,
        message="OK!",
        timestamp=datetime.now(),
        results=FaceAuthResult(match=True, similarity=0.95),
    )
    return response.model_dump()
