"""API that serves the lead evaluation functionality."""

from fastapi import FastAPI
from infrastructure.delivery.handler.validation_handler import validation_handler
from pydantic import BaseModel

app = FastAPI()


class LeadInfo(BaseModel):
    """lead informationrmation"""

    nin: int
    birthdate: str  # Este campo lo pasaria a un datetime por ej
    first_name: str
    last_name: str


@app.post("/evaluation")
def evaluation(data: LeadInfo) -> dict:
    """Evaluation endpoint.
    Args:
        leadinfo (dict): lead information
    Returns:
        dict: evaluation response with validation
    """
    validation = validation_handler(dict(data))
    return validation
