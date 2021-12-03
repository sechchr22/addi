# Hay que simular la latencia
# Como??
# con un wait.. sleep
import json
from time import sleep

from infrastructure.services.mock_response import MockResponse


def qualification_system_service() -> dict:
    sleep(3.0)
    response = MockResponse({"key1": "value1"}, 200)
    result = response.toJSON()
    return {"result": result}
