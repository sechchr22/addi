"""Validation handler in charge of lead validation."""
from bussines.usecases.national_archives_use_case import get_national_archives
from bussines.usecases.national_registry_use_case import get_national_registry
from bussines.usecases.qualification_use_case import get_qualification
from infrastructure.delivery.handler.error_handler import error_handler
from infrastructure.delivery.handler.utils.utils import (
    compair_with_national_registry,
    judicial_records,
    run_io_tasks_in_parallel,
)
from IPython.core.debugger import Pdb

ipdb = Pdb()

national_registry_key = "national_registry"
national_archives_key = "national_archives"
qualification_threshold = 60


def validation_handler(leadinfo: dict) -> dict:
    ipdb.set_trace()
    """Handles the lead validation.
    Args:
        leadinfo (dict): lead information
    Returns:
        dict: response with lead validation (lead or prospect).
    """
    # Getting lead information from services
    results = run_io_tasks_in_parallel(
        [
            lambda: get_national_registry(leadinfo),
            lambda: get_national_archives(leadinfo),
        ]
    )

    # lead information matching with national registry
    # and free of any judicial_record?
    for result in results:
        if national_registry_key in result:
            status = result[national_registry_key]["status_code"]
            # NOTA: acá el 200 es un ejemplo, deberia ser un 2xx
            if status != 200:
                return error_handler()
            comparision = compair_with_national_registry(
                leadinfo, result[national_registry_key]["response"]
            )
            continue
        if national_archives_key in result:
            status = result[national_archives_key]["status_code"]
            if status != 200:
                return error_handler()
            lead_judicial_records = judicial_records(result[national_archives_key])
            continue

    score = 0
    label = "lead"
    # If lead information match and doesnt have any judicial record
    # Gets qualified by system
    if comparision and not lead_judicial_records:
        qualification = get_qualification(leadinfo["nin"])
        response = qualification["qualification_system"]["response"]
        score = response["qualification"]

    if score > qualification_threshold:
        label = "prospect"

    return {"lead_nin": leadinfo["nin"], "evaluation": label, "score": score}
