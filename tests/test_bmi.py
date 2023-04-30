import pytest
from bmi import Bmi

def test_one():
    p1=Bmi(75, 170)
    assert p1.bmi==pytest.approx(25.95, .01)
    assert p1.category() == 'เกินเกณฑ์'

def test_two():
    p1=Bmi(48, 160)
    assert p1.bmi==pytest.approx(18.75, .01)
    assert p1.category() == 'ตามเกณฑ์'

def test_three():
    p1=Bmi(40, 160)
    assert p1.bmi==pytest.approx(15.62, .01)
    assert p1.category() == 'ต่ำกว่าเกณฑ์'