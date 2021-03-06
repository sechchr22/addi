""" Qualification system service."""
from time import sleep

from infrastructure.services.mock_response import MockResponse


def qualification_system_service(lead_nin: int) -> dict:
    """Request to qualification system service.
    Args:
        lead_nin (int): lead national identification number
    Returns:
        dict: response from qualification system service
    """
    sleep(3.0)
    response = MockResponse({"qualification": 65}, 200)
    # simulating exceptions handling
    if response.status_code != 200:
        # i would do it with an error_handler
        message = "error"
        response_dict["response"] = message
        response_dict["status"] = response.status_code
    else:
        response_dict = response.toJSON()
    return {"qualification_system": response_dict}
