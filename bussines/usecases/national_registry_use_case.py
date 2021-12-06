"""Get national registry from lead information."""
from infrastructure.services.national_registry_identification import (
    national_registry_identificaction_service,
)


def get_national_registry(leadinfo: dict) -> dict:
    """Get national registry.
    Args:
        leadinfo (dict): lead information
    Returns:
        dict: national registry from lead
    """
    return national_registry_identificaction_service(leadinfo)
