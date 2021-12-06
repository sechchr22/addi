"""Response service mock."""


class MockResponse:
    """Response Mock."""

    def __init__(self, json_data: dict, status_code: int):
        self.json_data = json_data
        self.status_code = status_code

    def toJSON(self):
        """Parses class instance to a dict.
        Returns:
            dict: dict representation of that instance.
        """
        JSON_dict = {"response": self.json_data, "status_code": self.status_code}
        return JSON_dict
