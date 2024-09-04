import sys
from typing import Iterator


def filter_by_currency(transactions: list, value: str) -> Iterator:
    """Функция возвращает операции в которых указана валюта"""
    if transactions == []:
        sys.exit("Нет транзакции")
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == value:
            yield transaction



def transaction_descriptions(transactions: list) -> Iterator:
    """Функция возвращает описание каждой операции"""
    if not transactions:
        sys.exit("Нет транзакции")
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Iterator:
    """Функция генерирует номера карт в заданном диапазоне"""
    for i in range(start, stop + 1):
        number_zero = "0000000000000000"
        card_number = number_zero[: -len(str(i))] + str(i)  # Генерация номера карты
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

