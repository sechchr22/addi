"""Get a lead qualification."""
from infrastructure.services.qualification_system import qualification_system_service


def get_qualification(lead_nin: int) -> dict:
    """Get lead qualification.
    Args:
        lead_nin (nin): leads national identification number
    Returns:
        dict: response from qualification system
    """
    return qualification_system_service(lead_nin)
