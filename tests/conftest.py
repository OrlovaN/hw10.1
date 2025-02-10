import pytest


@pytest.fixture
def card_number() -> str:
    return "2002 20XX XXXX 3003"

@pytest.fixture
def account_number() -> str:
    return "XX4305"

@pytest.fixture
def all_operations() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ]


@pytest.fixture # список, отсортированный по дате по убыванию
def descending_date() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ]

@pytest.fixture # # список, отсортированный по дате по возрастанию
def ascending_date() -> list:
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ]

@pytest.fixture
def input_data():
    return [("Maestro 1596837868705199", "Maestro 1596 83XX XXXX 5199"),
            ("Счет 64686473678894779589", "Счет XX9589")]
