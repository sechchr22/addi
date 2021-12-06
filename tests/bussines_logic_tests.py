"""Bussines logic testing."""
from infrastructure.delivery.handler.validation_handler import validation_handler
from infrastructure.services.mock_response import MockResponse
from IPython.core.debugger import Pdb

from tests.conftest import client, data

ipdb = Pdb()


""" def test_evaluation_returns_prospect_qualification_over_60():
    #OJO ACA NO QUIERO LLAMAR DIRECTAMENTE A LOS SERVICIOS
    #LOS TENGO QUE MOCKEAR
    response = client.post("/evaluation", json=data)
    assert response.status_code == 200
    assert response.json()["evaluation"] == "prospect" """


def test_evaluation_returns_lead_qualification_under_60(mocker):
    # ojo acá cuando ya se inicio el Test client en esa funcion
    # puede estar tomando ya la funcion como viene por eso no la mockea?
    mocked_qualification_system = mocker.patch(
        "infrastructure.delivery.handler.validation_handler.get_qualification"
    )
    mocked_qualification_system.return_value = MockResponse({"qualification": 55}, 200).toJSON
    response = client.post("/evaluation", json=data)
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


""" def test_lead_does_not_match_with_national_registry():
    #testeo que score venga 0 y que el qualification system no se llame

def test_lead_has_judicial_records(): """
