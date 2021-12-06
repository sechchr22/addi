"""Get national archives from lead information."""
from infrastructure.services.national_archives import national_archives_service


def get_national_archives(leadinfo: dict) -> dict:
    """Get national archives.
    Args:
        leadinfo (dict): lead information
    Returns:
        dict: national archives from lead
    """
    return national_archives_service(leadinfo)
