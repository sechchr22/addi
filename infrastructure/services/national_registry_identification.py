"""National registry service."""
from time import sleep

from infrastructure.services.mock_response import MockResponse


def national_registry_identificaction_service(leadinfo: dict) -> dict:
    """Request to national registry service.
    Args:
        leadinfo (dict): lead information
    Returns:
        dict: response from national registry service
    """
    sleep(5.0)
    response = MockResponse(
        {"nin": 12345, "birthdate": "22/05/1994", "first_name": "sergio", "last_name": "rueda"},
        200,
    )
    # simulating exceptions handling
    if response.status_code != 200:
        # i would do it with an error_handler
        message = "error"
        response_dict["response"] = message
        response_dict["status"] = response.status_code
    else:
        response_dict = response.toJSON()
    return {"national_registry": response_dict}
