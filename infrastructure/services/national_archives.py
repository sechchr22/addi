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
    sleep(2.0)
    response = MockResponse({"judicial_records": "clean"}, 200)
    response_dict = response.toJSON()
    return {"national_archives": response_dict}
