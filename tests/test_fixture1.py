import pytest
from mlib import price_vat

@pytest.fixture
def input_vat():
    return .07

def test_one(input_vat):
    assert price_vat(107, input_vat)==(100, 7)
    assert price_vat(100, input_vat)==(93.46, 6.54)

def test_two(input_vat):
    assert price_vat(214, input_vat)==(200, 14)