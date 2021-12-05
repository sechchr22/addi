"""Handler utilities."""
from concurrent.futures import ThreadPoolExecutor

def run_io_tasks_in_parallel(tasks) -> list:
    results = []
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            results.append(running_task.result())
        return results

def compair_with_national_registry(data: dict, base: dict) -> bool:
    # Return True if they are equal, False if they are different
    # ahora.. que pasa si en base que sería la respuesta del servicio
    # me trajera las llaves que quiero comparar iguales pero adicional 1 mas
    # eso haria que el == fallara ?? si no seria armar otro dict con base con esas
    # llaves que quiero comparar o irme por la comparacion larga .. podria asumirlo
    if data == base:
        return True
    return False
    """ for key, value in data.items():
        if key == "nin":
            if value != base[key]
                comparision = False
                break
            continue
        if key == "birthdate"
            if value != base[key]
                comparision = False
                break
            continue
        if key == "first_name"
            if value != base[key]
                comparision = False
                break
            continue
        if key == "last_name"
            if value != base[key]
                comparision = False
                break
            continue
    return comparision """

def judicial_records(data: dict)-> bool:
    if data["judicial_records"] != "clean":
        return False
    return True
