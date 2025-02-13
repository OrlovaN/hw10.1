def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Функция, возвращающая словари с ключом state"""
    state_lists: list = []
    for operation in operations:
        if operation["state"] == state:
            state_lists.append(operation)
    return state_lists


def sort_by_date(operations: list, descending: bool = True) -> list:
    """Функция сортировки списка по дате"""
    return sorted(operations, key=lambda operation: operation["date"], reverse=descending)

