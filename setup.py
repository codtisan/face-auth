from dotenv import load_dotenv
import os
from app.databases.qdrant import Qdrant
import asyncio

load_dotenv()


async def check_store_directory() -> None:
    is_directory = os.path.isdir("stores")
    if not is_directory:
        os.mkdir("stores")


async def check_vectorstore_collection() -> None:
    if os.getenv('VECTOR_DB') == 'local':
        return
    qdrant = Qdrant()
    is_exist = await qdrant.check_exist("face_data")
    if not is_exist:
        await qdrant.create_collection("face_data", 512)


async def setup() -> None:
    print("Checking stores directory if exists or create it")
    await check_store_directory()
    print("Checking vector store collection if exists or create it")
    await check_vectorstore_collection()


asyncio.run(setup())
