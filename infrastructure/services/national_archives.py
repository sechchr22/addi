"""National archives service."""

from time import sleep

from infrastructure.services.mock_response import MockResponse


def national_archives_service(leadinfo: dict) -> dict:
    """Request to national archive service.
    Args:
        leadinfo (dict): lead information
    Returns:
        dict: response from national archive service
    """
    response_dict = {}
    sleep(2.0)
    response = MockResponse({"judicial_records": "clean"}, 200)
    # simulating exceptions handling
    if response.status_code != 200:
        # i would do it with an error_handler
        message = "error"
        response_dict["response"] = message
        response_dict["status"] = response.status_code
    else:
        response_dict = response.toJSON()
    return {"national_archives": response_dict}
