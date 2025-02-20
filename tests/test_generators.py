import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_1(transactions: list) -> None:
    """Проверяет корректность фильтровки транзакций по заданной валюте"""
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(usd_transactions) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_2(transactions: list) -> None:
    """Проверяем, что функция правильно обрабатывает случаи, если code пустой"""
    empty_trans = filter_by_currency(transactions, "")
    assert list(empty_trans) == []


def test_filter_by_currency_3(transactions: list) -> None:
    """Проверяем, что функция правильно обрабатывает случаи, если операции в заданной валюте отсутствуют"""
    GBP_trans = filter_by_currency(transactions, "GBP")
    assert list(GBP_trans) == []


def test_filter_by_currency_4(transactions: list) -> None:
    """Проверяем, что функция правильно обрабатывает случаи, если отсутствует ключ code"""
    missing_trans = filter_by_currency(transactions, "None")
    assert list(missing_trans) == []


@pytest.mark.parametrize(
    "value, code, expected",
    [
        ([{"operationAmount": {"currency": {"code": ""}}}], "USD", []),
        ([{"operationAmount": {"currency": {}}}], "USD", []),
        ([{"operationAmount": {}}], "USD", []),
        ([{"operationAmount": {"currency": {"code": "EUR"}}}], "USD", []),
        ([{"operationAmount": {"currency": {"code": None}}}], "USD", []),
    ],
)
def test_filter_by_currency_5(value: list, code: str, expected: list) -> None:
    # trans = filter_by_currency(value) == expected
    assert list(filter_by_currency(value, code)) == expected


def test_transaction_descriptions_1(transactions: list[dict]) -> None:
    """Проверяем, что функция возвращает корректные описания для каждой транзакции"""
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


@pytest.mark.parametrize(
    "value, expected",
    [
        # Пустой список транзакций
        ([], []),
        # Одна транзакция
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            ["Перевод организации"],
        ),
        # Все транзакции
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
        # Первые две транзакция без описания (проверяем, что пропускается)
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
        # Первая и последняя трансакции
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {},
                {},
                {},
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            ["Перевод организации", "Перевод организации"],
        ),
    ],
)
def test_transaction_descriptions_2(value: list[dict], expected: list[str]) -> None:
    """Тестируем функцию transaction_descriptions с различным количеством входных транзакций,
    включая пустой список"""
    assert list(transaction_descriptions(value)) == expected


def test_card_number_generator_1() -> None:
    """Проверяем, что генератор выдает правильные номера карт в заданном диапазоне"""
    start = 1234567890123456
    stop = 1234567890123459
    expected_numbers = [
        "1234 5678 9012 3456",
        "1234 5678 9012 3457",
        "1234 5678 9012 3458",
        "1234 5678 9012 3459",
    ]
    assert list(card_number_generator(start, stop)) == expected_numbers


def test_card_number_generator_2() -> None:
    """Проверяем, что генератор правильно обрабатывает случай, когда start и stop содержат только одну цифру."""
    start = 5
    stop = 5
    expected_numbers = ["0000 0000 0000 0005"]
    assert list(card_number_generator(start, stop)) == expected_numbers


def test_card_number_generator_3() -> None:
    """Проверяем, что генератор корректно обрабатывает крайние значения диапазона."""
    start = 0
    stop = 1
    expected_numbers = ["0000 0000 0000 0000", "0000 0000 0000 0001"]
    assert list(card_number_generator(start, stop)) == expected_numbers


def test_card_number_generator_4() -> None:
    """Проверяем, что генератор корректно обрабатывает полный диапазон."""
    start = 9999999999999995
    stop = 9999999999999999
    expected_numbers = [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
    assert list(card_number_generator(start, stop)) == expected_numbers


def test_card_number_generator_5() -> None:
    """Проверяем, что генератор возвращает пустой список, если start > stop."""
    start = 10
    stop = 5
    assert list(card_number_generator(start, stop)) == []  # range(10, 6) возвращает пустую последовательность


def test_card_number_generator_6() -> None:
    """Проверяем работу генератора на большом диапазоне."""
    start = 9999999999999990
    stop = 9999999999999993
    expected_numbers = [
        "9999 9999 9999 9990",
        "9999 9999 9999 9991",
        "9999 9999 9999 9992",
        "9999 9999 9999 9993",
    ]
    assert list(card_number_generator(start, stop)) == expected_numbers


def test_card_number_generator_7() -> None:
    """Проверяем, что при start = stop = 0 генерируется корректный номер."""
    start = 0
    stop = 0
    expected_numbers = ["0000 0000 0000 0000"]
    assert list(card_number_generator(start, stop)) == expected_numbers


@pytest.mark.parametrize(
    "start, stop",
    [
        (-1, 5),
        (5, 10000000000000000),
        (10000000000000000, 10000000000000005),
    ],
)
def test_card_number_generator_8(start: int, stop: int) -> None:
    """Проверяем, что функция возвращает None при некорректном диапазоне."""
    assert list(card_number_generator(start, stop)) == []
