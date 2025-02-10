import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import all_operations


def test_filter_by_state(all_operations: list) -> None:
    """Функция тестирования фильтрации по статусу"""
    assert filter_by_state(all_operations,  "EXECUTED") == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
       ]

@pytest.mark.parametrize("state, expected",
                         [
("EXECUTED", [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
("CANCELED", [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
("HOVERING", []),
("", [])
])
def test_filter_by_state_2(all_operations: list, state: str, expected: list) -> None:
    """Функция тестирования фильтрации с помощью параметризации"""
    assert filter_by_state(all_operations, state) == expected



def test_sort_by_date(all_operations: list, descending_date: list) -> None:
    """Функция тестирования по дате в порядке убыванию"""
    assert (sort_by_date(all_operations) == descending_date)


def test_sort_by_date_2(all_operations: list, ascending_date: list) -> None:
    """Функция тестирования по дате в порядке возрастания"""
    assert (sort_by_date(all_operations, reverse=False) == ascending_date)


@pytest.mark.parametrize(
    "value, expected",
    [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-14T21:27:25.241689'}],
      [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-14T21:27:25.241689'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
    ])
def test_sort_by_date_3(value: list, expected: list) -> None:
    """Функция для теста сортировки по дате с помощью параметризации"""
    assert (sort_by_date(value) == expected)
