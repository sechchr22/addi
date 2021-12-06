"""Validation handler in charge of lead validation."""
from bussines.usecases.national_archives_use_case import get_national_archives
from bussines.usecases.national_registry_use_case import get_national_registry
from bussines.usecases.qualification_use_case import get_qualification
from infrastructure.delivery.handler.utils.utils import (
    compair_with_national_registry,
    judicial_records,
    run_io_tasks_in_parallel,
)

national_registry_key = "national_registry"
national_archives_key = "national_archives"
qualification_threshold = 60


def validation_handler(leadinfo: dict) -> dict:
    """Handles the lead validation.
    Args:
        leadinfo (dict): lead information
    Returns:
        dict: response with lead validation (lead or prospect).
    """
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
            comparision = compair_with_national_registry(
                leadinfo, result[national_registry_key]
            )
            continue
        if national_archives_key in result:
            lead_judicial_records = judicial_records(result[national_archives_key])
            continue

    score = 0
    # If lead information match and doesnt have any judicial record
    # Gets qualified by system
    if comparision and lead_judicial_records:
        qualification = get_qualification(leadinfo["nin"])
        score = qualification["qualfication_system"]["qualification"]

    if score > qualification_threshold:
        return {"evaluation": "prospect"}

    return {"evaluation": "lead"}
