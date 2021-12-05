# Hay que simular la latencia
# Como??
# con un wait.. sleep
import json
from time import sleep

from infrastructure.services.mock_response import MockResponse


def qualification_system_service() -> dict:
    sleep(3.0)
    response = MockResponse({"qualification": 65}, 200)
    response_dict = response.toJSON()
    return {"qualification_system": response_dict}
