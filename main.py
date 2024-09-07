from app.server import app
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()


def bootstrap() -> None:
    port = int(os.getenv("PORT"))
    uvicorn.run(app=app, port=port, host="0.0.0.0")


bootstrap()
