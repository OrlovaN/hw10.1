import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency():
    assert filter_by_currency()

@pytest.mark.parametrize(
        "value, expected", []
        [