from app.bases.vectorstore import VectorDatabaseBase
from dotenv import load_dotenv
import os
from qdrant_client import AsyncQdrantClient, models

load_dotenv()


class Qdrant(VectorDatabaseBase):
    def __init__(self, url: str = os.getenv("VECTOR_DB_URL")) -> None:
        super().__init__()
        self.client = AsyncQdrantClient(url=url)

    async def create_collection(
        self, collection_name: str, vector_size: int, distance_method: str = "Cosine"
    ) -> None:
        if not await self.client.collection_exists(collection_name):
            await self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size, distance=distance_method
                ),
            )
        return

    async def insert(
        self, collection_name: str, payload: dict, id: str, vector: list[float]
    ) -> None:
        await self.client.upsert(
            collection_name=collection_name,
            points=[models.PointStruct(id=id, vector=vector, payload=payload)],
        )
        return

    async def batch_insert(
        self,
        collection_name: str,
        payloads: list[dict],
        ids: list[str],
        vectors: list[list[float]],
    ) -> None:
        points_struct = []
        for index in range(len(vectors)):
            points_struct.append(
                models.PointStruct(
                    id=ids[index], vector=vectors[index], payload=payloads[index]
                )
            )
        await self.client.upsert(
            collection_name=collection_name,
            points=points_struct,
        )
        return

    async def upsert(self, collection_name: str, payload: dict, id: str, vector: list[float]) -> None:
        if not await self.client.collection_exists(collection_name):
            await self.client.upsert(
                collection_name=collection_name,
                points=[models.PointStruct(id=id, vector=vector, payload=payload)],
            )
        return

    async def check_exist(self, collection_name: str) -> bool:
        is_exist = await self.client.collection_exists(collection_name=collection_name)
        return is_exist
    
    async def search(self, collection_name: str, limit: int, query_vector: list[float]) -> None:
        response = await self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,  # type: ignore
            limit=limit,
        )
        return response