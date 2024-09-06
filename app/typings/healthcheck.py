from pydantic import BaseModel
from datetime import datetime

class HealthResponse(BaseModel):
    status: str
    status_code: int
    message: str
    timestamp: datetime
