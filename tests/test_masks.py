import pytest
from src.masks import get_mask_card, get_mask_account


@pytest.mark.parametrize("num_card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007922896063", 'Неправильный ввод карты!!!')
    ],
)


def test_get_mask_card(num_card, expected):
    assert get_mask_card(num_card) == expected


@pytest.mark.parametrize(
    "num_account, expected_acc",
    [
        ("73654108430135874305", "**4305"),
        ("7365410843013587", "Неправильный ввод номера счёта!!!"),

    ],
)
def test_get_mask_account(num_account, expected_acc):
    assert get_mask_account(num_account) == expected_acc
