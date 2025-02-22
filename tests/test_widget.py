import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    """Функция для обработки информации о картах через assert"""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79XX XXXX 6361"
    assert mask_account_card("Счет 64686473678894779589") == "Счет XX9589"


@pytest.mark.parametrize(
    "value, expected",
    [("Maestro 1596837868705199", "Maestro 1596 83XX XXXX 5199"), ("Счет 64686473678894779589", "Счет XX9589")],
)
def test_mask_account_card_2(value: str, expected: str) -> None:
    """Функция для обработки информации о картах через параметризацию"""
    assert mask_account_card(value) == expected


def test_mask_account_card_3() -> None:
    with pytest.raises(Exception):
        mask_account_card("")


def test_get_date() -> None:
    """Функция проверки преобразования формата даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        (" ", "не введена дата"),
        ("11/03/2024", "некорректный формат даты"),
    ],
)
def test_get_date_2(value: str, expected: str) -> None:
    assert get_date(value)
