import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_1() -> None:
    """Функция для теста маскировки номера карты через assert"""
    assert get_mask_card_number("7000792289606361") == "7000 79XX XXXX 6361"


def test_get_mask_card_number_2(card_number: str) -> None:
    """Функция для теста маскировки номера карты с помощью фикстур"""
    assert get_mask_card_number("2002200230033003") == card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2002200230033003", "2002 20XX XXXX 3003"),
        ("5555201234561111", "5555 20XX XXXX 1111"),
        ("", "не введен номер карты"),
        ("2002", "неверно введен номер карты"),
        ("2002 3003 4004 5005 6006 6", "неверно введен номер карты"),
        ("FDCBH", "неверно введен номер карты"),
    ],
)
def test_get_mask_card_number_3(value: str, expected: str):
    """Функция для теста маскировки номера карты с помощью параметризации"""
    assert get_mask_card_number(value) == expected


def test_get_mask_account() -> None:
    """Функция для теста маскировки номера счета через assert"""
    assert get_mask_account("73654108430135874305") == "XX4305"


def test_get_mask_account_2(account_number: str) -> None:
    """Функция для теста маскировки номера счета с помощью фикстур"""
    assert get_mask_account("73654108430135874305") == account_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "XX4305"),
        ("28632743123265489575", "XX9575"),
        ("", "не введен номер счета"),
        ("5678", "неверно введен номер счета"),
        ("FDCBH", "неверно введен номер счета"),
    ],
)
def test_get_mask_account_3(value: str, expected: str) -> None:
    """Функция для теста маскировки номера счета с помощью параметризации"""
    assert get_mask_card_number(value)
