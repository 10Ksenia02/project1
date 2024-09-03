from typing import Any

# '''Функция которая принимает список словарей'''


def filter_by_state(new_list, state="EXECUTED"):

    result = []
    for key in new_list:
        if key.get('state') == state:
            result.append(key)
    return result


def sort_by_date(new_list: list, old_data=True):
    sorted_list = sorted(new_list, key=lambda i: i["date"], reverse=old_data)
    return sorted_list
