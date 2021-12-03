# Hay que simular la latencia
# Como??
# con un wait.. sleep

from time import sleep

from infrastructure.services.mock_response import MockResponse
from IPython.core.debugger import Pdb

ipdb = Pdb()


async def national_archives_service(nin: int) -> dict:
    sleep(2.0)
    response = MockResponse({"key1": "value1"}, 200)
    result = response.toJSON()
    return {"result": result}
