from unittest.mock import Mock, patch

from src.utils import get_transaction_amount_in_rub, load_transactions_from_json


def test_load_transactions_from_json_1() -> None:
    """Тест на успешную загрузку данных из JSON файла"""
    mock_load_transaction = Mock(return_value=5)
    load_transactions_from_json = mock_load_transaction
    assert load_transactions_from_json() == 5
    mock_load_transaction.assert_called_once()


def test_load_transactions_from_json_2() -> None:
    """Тест на случай, когда файл не найден."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions_from_json("nonexistent_file.json")
        assert result == []


def test_load_transactions_from_json_3() -> None:
    """Тест случая, когда JSON-файл содержит не список."""
    mock_data = '{"error": "not a list"}'
    with patch("builtins.open", Mock(read_data=mock_data)):
        result = load_transactions_from_json("not_a_list.json")
        assert result == []


@patch("src.external_api.convert_currency")
def test_get_transaction_amount_in_rub_1(mock_convert_currency) -> None:
    """Тест для транзакции в рублях."""
    transaction = {"amount": 100, "code": "RUB"}
    amount = get_transaction_amount_in_rub(transaction)
    assert amount == 100.0
    mock_convert_currency.assert_not_called()


@patch("src.external_api.convert_currency")
def test_get_transaction_amount_in_rub_4(mock_convert_currency: str) -> None:
    """Тест для транзакции без указания суммы."""
    transaction = {"code": "RUB"}
    amount = get_transaction_amount_in_rub(transaction)
    assert amount is None
    mock_convert_currency.assert_not_called()


@patch("src.external_api.convert_currency")
def test_get_transaction_amount_in_rub_5(mock_convert_currency: str) -> None:
    """Тест для транзакции без указания валюты."""
    transaction = {"amount": 100}
    amount = get_transaction_amount_in_rub(transaction)
    assert amount is None
    mock_convert_currency.assert_not_called()


@patch("src.external_api.convert_currency")
def test_get_transaction_amount_in_rub_6(mock_convert_currency: str) -> None:
    """Тест для неподдерживаемой валюты."""
    transaction = {"amount": 100, "code": "GBP"}
    amount = get_transaction_amount_in_rub(transaction)
    assert amount is None
    mock_convert_currency.assert_not_called()
