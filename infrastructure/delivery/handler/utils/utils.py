"""Handler utilities."""
from concurrent.futures import ThreadPoolExecutor
from types import FunctionType
from typing import List


def run_io_tasks_in_parallel(tasks: List[FunctionType]) -> list:
    """Run a list of tasks/functions in parallel.
    Args:
        tasks (dict): lead information
    Returns:
        list: list of tasks/functions return values.
    """
    results = []
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            results.append(running_task.result())
        return results


def compair_with_national_registry(data: dict, base: dict) -> bool:
    """Compare two dictionaries to check if they are identical.
    Args:
        data (dict): dict to compare.
        base (dict): base dict to compare.
    Returns:
        bool: True if both dict are identical, False otherwise.
    """
    if data == base:
        return True
    return False


def judicial_records(data: dict) -> bool:
    """Check if lead has any judicial record.
    Args:
        data (dict): lead information.
    Returns:
        bool: True if lead has at least one judicial record, False otherwise.
    """
    response = data["response"]
    if response["judicial_records"] != "clean":
        return True
    return False
