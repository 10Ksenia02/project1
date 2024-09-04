# '''Функция которая принимает список словарей'''


def filter_by_state(new_list: list, state="EXECUTED") -> list:
    result = []
    for new_lists in new_list:
        for i, v in new_lists.items():
            if v == state:
                result.append(new_lists)
    return result


def sort_by_date(new_list: list, old_data=True):
    sorted_list = sorted(new_list, key=lambda i: i["date"], reverse=old_data)
    return sorted_list
