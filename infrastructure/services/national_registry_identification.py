# Hay que simular la latencia
# Como??
# con un wait.. sleep
import json
from time import sleep

from infrastructure.services.mock_response import MockResponse


async def national_registry_identificaction_service(nin: int) -> dict:
    # Hago una llamada al servicio
    # el servicio me traeria información de un lead
    sleep(1.0)
    response = MockResponse({"key1": "value1"}, 200)
    result = response.toJSON()
    return {"result": result}
