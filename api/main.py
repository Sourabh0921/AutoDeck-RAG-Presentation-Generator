import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI

from api.routes.presentation import (
    router
)

app = FastAPI(
    title=
    "AutoDeck Presentation Generator"
)

app.include_router(
    router,
    prefix="/api"
)


@app.get("/")
def home():

    return {
        "message":
        "AutoDeck API Running"
    }