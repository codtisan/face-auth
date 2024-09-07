from app.server import app
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()


def bootstrap() -> None:
    is_directory = os.path.isdir("stores")
    if not is_directory:
        os.mkdir("stores")
    port = int(os.getenv("PORT"))
    uvicorn.run(app=app, port=port, host="0.0.0.0")


bootstrap()
