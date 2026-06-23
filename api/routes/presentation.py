import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from fastapi import APIRouter

from api.schemas.request_schema import (
    PresentationRequest
)

from src.chains.presentation_chain import (
    PresentationChain
)

router = APIRouter()

presentation_chain = (
    PresentationChain()
)


@router.post(
    "/generate"
)
def generate_presentation(
    request:
    PresentationRequest
):

    result = (
        presentation_chain
        .generate_presentation(
            request.topic
        )
    )

    return result