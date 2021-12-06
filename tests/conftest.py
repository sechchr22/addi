"""Testing config."""
from fastapi import FastAPI
from fastapi.testclient import TestClient
from infrastructure.delivery.api import LeadInfo
from infrastructure.delivery.handler.validation_handler import validation_handler

app = FastAPI()

# it has to match with the response of the national registry
data = {
    "nin": 12345,
    "birthdate": "22/05/1994",
    "first_name": "sergio",
    "last_name": "rueda",
}


@app.post("/evaluation")
def evaluation_testing(data: LeadInfo) -> dict:
    validation = validation_handler(dict(data))
    return validation


client = TestClient(app)
