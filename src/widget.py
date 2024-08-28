from src.masks import get_mask_account, get_mask_card

def get_mask_account(number: str) -> str:
    """ Функция получает строку и маскирует счет/карту """
    if len(number.split()[-1]) == 16:
        new_number = get_mask_card(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        # return result
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
    return result


if __name__ == '__main__':
    print(get_mask_account('Счет 12345678901234567890'))
    print(get_mask_account('Visa Classic 1234567890123456'))
    # должно вывестись в терминал
    # Счет **7890
    # Visa Classic 1234 56** **** 3456


def get_new_data(old_data: str) -> str:
    """ Функция принимает строку с датой и
    выводит в формате dd.mm.yyyy """

    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])
