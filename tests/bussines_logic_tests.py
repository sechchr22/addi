"""Bussines logic testing."""
from infrastructure.delivery.handler.validation_handler import validation_handler
from infrastructure.services.mock_response import MockResponse

from tests.conftest import client, data


def test_evaluation_returns_prospect_qualification_over_60(mocker):
    # testeo que si la calificación es sobre 60 la evaluación sea prospect
    mocked_national_registry = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_national_registry"
    )
    response = MockResponse(
        {
            "nin": 12345,
            "birthdate": "22/05/1994",
            "first_name": "sergio",
            "last_name": "rueda",
        },
        200,
    )
    mocked_national_registry.return_value = {"national_registry": response.toJSON()}
    mocked_national_archives = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_national_archives"
    )
    response = MockResponse({"judicial_records": "clean"}, 200)
    mocked_national_archives.return_value = {"national_archives": response.toJSON()}
    mocked_qualification_system = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_qualification"
    )
    response = MockResponse({"qualification": 65}, 200)
    mocked_qualification_system.return_value = {"qualification_system": response.toJSON()}
    response = client.post("/evaluation", json=data)
    assert response.status_code == 200
    assert response.json()["evaluation"] == "prospect"


def test_evaluation_returns_lead_qualification_under_60(mocker):
    # testeo que si la calificación es abajo de 60 la evaluación sea lead
    mocked_national_registry = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_national_registry"
    )
    response = MockResponse(
        {
            "nin": 12345,
            "birthdate": "22/05/1994",
            "first_name": "sergio",
            "last_name": "rodriguez",
        },
        200,
    )
    mocked_national_registry.return_value = {"national_registry": response.toJSON()}
    mocked_national_archives = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_national_archives"
    )
    response = MockResponse({"judicial_records": "clean"}, 200)
    mocked_national_archives.return_value = {"national_archives": response.toJSON()}
    mocked_qualification_system = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_qualification"
    )
    response = MockResponse({"qualification": 55}, 200)
    mocked_qualification_system.return_value = {"qualification_system": response.toJSON()}
    response = client.post("/evaluation", json=data)
    assert response.status_code == 200
    assert response.json()["evaluation"] == "lead"


def test_lead_does_not_match_with_national_registry(mocker):
    # testeo que score venga 0 y que el qualification system no se llame
    # cuando no hay un match con la informacion del national_registry_service
    mocked_national_registry = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_national_registry"
    )
    response = MockResponse(
        {
            "nin": 12345,
            "birthdate": "22/05/1994",
            "first_name": "sergio",
            "last_name": "rodriguez",
        },
        200,
    )
    mocked_national_registry.return_value = {"national_registry": response.toJSON()}
    mocked_national_archives = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_national_archives"
    )
    response = MockResponse({"judicial_records": "clean"}, 200)
    mocked_national_archives.return_value = {"national_archives": response.toJSON()}
    mocked_qualification_system = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_qualification"
    )
    response = MockResponse({"qualification": 55}, 200)
    mocked_qualification_system.return_value = {"qualification_system": response.toJSON()}
    response = client.post("/evaluation", json=data)
    assert response.status_code == 200
    assert response.json()["evaluation"] == "lead"
    assert response.json()["score"] == 0
    assert not mocked_qualification_system.called


def test_lead_has_judicial_records(mocker):
    # testeo que score venga 0 y que el qualification system no se llame
    # cuando el lead tenga algun pasado judicial
    mocked_national_registry = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_national_registry"
    )
    response = MockResponse(
        {
            "nin": 12345,
            "birthdate": "22/05/1994",
            "first_name": "sergio",
            "last_name": "rueda",
        },
        200,
    )
    mocked_national_registry.return_value = {"national_registry": response.toJSON()}
    mocked_national_archives = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_national_archives"
    )
    response = MockResponse({"judicial_records": "not_clean"}, 200)
    mocked_national_archives.return_value = {"national_archives": response.toJSON()}
    mocked_qualification_system = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_qualification"
    )
    response = MockResponse({"qualification": 55}, 200)
    mocked_qualification_system.return_value = {"qualification_system": response.toJSON()}
    response = client.post("/evaluation", json=data)
    assert response.status_code == 200
    assert response.json()["evaluation"] == "lead"
    assert response.json()["score"] == 0
    assert not mocked_qualification_system.called
