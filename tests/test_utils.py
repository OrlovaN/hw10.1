import pytest
from unittest.mock import Mock, patch


def test_load_transactions_from_json():
    """"""
    mock_load_transaction = Mock(return_value=5)
    load_transactions_from_json = mock_load_transaction
    assert load_transactions_from_json() == 5
    mock_load_transaction.assert_called_once()


@patch



