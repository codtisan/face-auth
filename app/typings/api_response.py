from pydantic import BaseModel
from datetime import datetime


class FaceRegistrationResult(BaseModel):
    success: bool


class FaceRegistrationResponse(BaseModel):
    status: str
    status_code: int
    message: str
    timestamp: datetime
    results: FaceRegistrationResult


class FaceAuthResult(BaseModel):
    match: bool
    similarity: float


class FaceAuthResponse(BaseModel):
    status: str
    status_code: int
    message: str
    timestamp: datetime
    results: FaceAuthResult
