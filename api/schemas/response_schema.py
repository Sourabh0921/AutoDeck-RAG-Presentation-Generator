from pydantic import BaseModel
from typing import List


class Slide(
    BaseModel
):

    title: str

    bullets: List[str]

    source: str


class PresentationResponse(
    BaseModel
):

    slides: List[Slide]