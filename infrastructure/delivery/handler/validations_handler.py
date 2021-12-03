# Validation Handler
# In charge of prospect validation

from infrastructure.services.national_archives import national_archives_service
from infrastructure.services.national_registry_identification import (
    national_registry_identificaction_service,
)


async def validation_handler(leadinfo: int) -> str:

    # En paralelo llamo
    national_registry = await national_registry_identificaction_service(
        leadinfo
    )  # esto me treaeria la info del national registry
    national_archives = await national_archives_service(
        leadinfo
    )  # esto me traeria la info de los archivos nacionales

    # matching_national_registry(national_registry)  # y esto seria un booleano.
    # judicial_records(
    # national_archives
    # )  # y esto seria booleano. # o puede que si len de national_archives es 0 es que no tiene.

    # SI TODO ESTA EN ORDEN osea los 2 de arriba me dan True
    # evaluation = qualification_system(leadinfo)
    evaluation = "lead"

    return evaluation
