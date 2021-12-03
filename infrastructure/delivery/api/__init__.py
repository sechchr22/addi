import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

from infrastructure.delivery.handler.validations_handler import validation_handler


class LeadInfo(BaseModel):
    nin: int
    birthdate: str
    first_name: str
    last_name: str


@app.post("/evaluation")
async def evluation(data: LeadInfo):
    start = time.time()
    validation = await validation_handler(4)
    end = time.time()
    execution_time = end - start
    print("EXECUTION_TIME: {}".format(execution_time))
    return {"validation": validation}
