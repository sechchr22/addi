# Hay que simular la latencia
# Como??
# con un wait.. sleep

from time import sleep

from infrastructure.services.mock_response import MockResponse


def national_archives_service(nin: int) -> dict:
    sleep(2.0)
    response = MockResponse({"judicial_records": "clean"}, 200)
    response_dict = response.toJSON()
    return {"national_archives": response_dict}
