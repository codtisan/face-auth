from fastapi import FastAPI, UploadFile, File
from datetime import datetime
from app.typings.healthcheck import HealthResponse
from app.typings.api_response import (
    FaceAuthResponse,
    FaceRegistrationResponse,
    FaceRegistrationResult,
    FaceAuthResult,
)
import uuid
from PIL import Image
import io
import os
from deepface import DeepFace
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import asyncio

app = FastAPI()
threshold = 0.9


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
async def register(file: UploadFile = File(...)) -> FaceRegistrationResponse:
    contents = file.file.read()
    image = Image.open(io.BytesIO(contents))
    user_id = str(uuid.uuid4())
    filename = "face.jpg"
    image_path = f"stores/{user_id}/{filename}"

    os.mkdir(f"stores/{user_id}")
    image.save(image_path)

    result = DeepFace.represent(img_path=image_path)

    np.save(f"stores/{user_id}/embedding.npy", result[0]["embedding"])

    response = FaceRegistrationResponse(
        status="success",
        status_code=201,
        message="OK!",
        timestamp=datetime.now(),
        results=FaceRegistrationResult(success=True),
    )
    return response.model_dump()


@app.post("/auth")
async def authenticate(file: UploadFile = File(...)) -> FaceAuthResponse:
    contents = file.file.read()
    image = Image.open(io.BytesIO(contents))

    image_matrix = np.array(image)

    result = DeepFace.represent(img_path=image_matrix)
    embedding = np.array(result[0]["embedding"])

    user_dirs = os.listdir("stores")

    async def get_embedding(dir: str):
        return np.load(f"stores/{dir}/embedding.npy")

    task = [get_embedding(dir) for dir in user_dirs]
    all_embeddings = await asyncio.gather(*task)

    similarity_results = cosine_similarity([embedding], all_embeddings)[0]
    highest_similarity = similarity_results.max()

    is_match = highest_similarity >= threshold

    response = FaceAuthResponse(
        status="success",
        status_code=201,
        message="OK!",
        timestamp=datetime.now(),
        results=FaceAuthResult(match=is_match, similarity=highest_similarity),
    )
    return response.model_dump()
