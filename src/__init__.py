import uvicorn

from src.app import app
from src.config import PORT


def run():
    uvicorn.run("src:app", port=PORT)


def dev():
    uvicorn.run("src:app", port=PORT, reload=True)
