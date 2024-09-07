from abc import ABC, abstractmethod


class VectorDatabaseBase(ABC):
    @abstractmethod
    async def create_collection(self, collection_name: str, vector_size: int, distance_method: str) -> None:
        pass

    @abstractmethod
    async def insert(self, collection_name: str, payload: dict, id: str, vector: list[float]) -> None:
        pass

    @abstractmethod
    async def batch_insert(self, collection_name: str, payloads: list[dict], ids: list[str], vectors: list[list[float]]) -> None:
        pass

    @abstractmethod
    async def upsert(self, collection_name: str, payload: dict, id: str, vector: list[float]) -> None:
        pass

    @abstractmethod
    async def check_exist(self, collection_name: str) -> None:
        pass

    @abstractmethod
    async def search(self, collection_name: str, limit: int, query_vector: list[float]) -> None:
        pass