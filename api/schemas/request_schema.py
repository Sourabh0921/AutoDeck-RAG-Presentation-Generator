from pydantic import BaseModel


class PresentationRequest(
    BaseModel
):

    topic: str