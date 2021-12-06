# Hay que simular la latencia
# Como??
# con un wait.. sleep
import json
from time import sleep

from infrastructure.services.mock_response import MockResponse


def national_registry_identificaction_service(leadinfo: dict) -> dict:
    # Hago una llamada al servicio
    # el servicio me traeria información de un lead
    sleep(5.0)
    response = MockResponse(
        {
            "nin": "12345",
            "birthdate": "22/05/1994",
            "first_name": "sergio",
            "last_name": "rueda"
        }, 200
    )
    response_dict = response.toJSON()
    return {"national_registry": response_dict}
