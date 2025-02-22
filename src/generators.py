from typing import Generator

transactions = [
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
]


def filter_by_currency(transactions: list[dict], code: str) -> Generator[dict]:
    """Функция фильтрует список транзакций и возвращает итератор, выдающий только транзакции с заданной валютой"""
    if code is None:
        return
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount")
        if operation_amount:
            currency = operation_amount.get("currency")
            if currency and currency.get("code") == code:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Функция возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        description = transaction.get("description")
        if isinstance(description, str) and description:  # Проверяем, что описание - строка и не пустое
            yield description


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция генерации номеров банковских карт"""
    if not (0 <= start <= stop <= 9999999999999999):
        return
    for number in range(start, stop + 1):
        number_str = str(number)
        str_length = 16 - len(number_str)  # Добавляем ведущие нули вручную, если длина строки меньше 16
        if str_length > 0:
            number_str = "0" * str_length + number_str
        if len(number_str) < 16:
            number_str = "0" * (16 - len(number_str)) + number_str
        formatted_card_number = " ".join(number_str[i : i + 4] for i in range(0, 16, 4))
        yield formatted_card_number
