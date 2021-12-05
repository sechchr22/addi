import time

from fastapi import FastAPI
from pydantic import BaseModel
from IPython.core.debugger import Pdb

ipdb = Pdb()


app = FastAPI()

from infrastructure.delivery.handler.validations_handler import validation_handler


class LeadInfo(BaseModel):
    nin: int
    birthdate: str
    first_name: str
    last_name: str


@app.post("/evaluation")
def evluation(data: LeadInfo):
    ipdb.set_trace()
    start = time.time()
    validation = validation_handler(4)
    end = time.time()
    execution_time = end - start
    print("EXECUTION_TIME: {}".format(execution_time))
    return {"validation": validation}
