# Validation Handler
# In charge of prospect validation
from infrastructure.delivery.handler.utils.utils import (
    run_io_tasks_in_parallel,
    compair_with_national_registry,
    judicial_records,
)
from infrastructure.services.national_archives import national_archives_service
from infrastructure.services.national_registry_identification import (
    national_registry_identificaction_service,
)
from infrastructure.services.qualification_system import 

national_registry_key = "national_registry"
national_archives_key = "national_archives"

def validation_handler(leadinfo: int) -> dict:
    # Bringing lead info
    results = run_io_tasks_in_parallel(
        [
            lambda: national_registry_identificaction_service(leadinfo),
            lambda: national_archives_service(leadinfo),
        ]
    )

    # Lead info matching with national registry and free of any judicial_record?
    for result in results:
        if national_registry_key in result:
            comparision = compair_with_national_registry(leadinfo, result[national_registry_key])
        if national_archives_key in result:
            judicial_records = judicial_records(result[national_archives_key])
    
    if comparision and judicial_records:
        qualification = qualification_system_service(nin)
        score = qualification["qualfication_system"]["qualification"]
    
    if score > 60:
        return {"evaluation": "prospect"}
    
    return {"evaluation": "lead"}
