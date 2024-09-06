from abc import ABC, abstractmethod


class VectorDatabaseBase(ABC):
    @abstractmethod
    async def create_collection(self, alias: str, vector_size: int, distance_method: str) -> None:
        pass