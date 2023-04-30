# doc https://docs.pytest.org/en/stable/index.html

from area import rectangle, triangle
from volume import *
import pytest


def test_one():
    assert rectangle(5, 2) == 10
    assert rectangle(5, 2) == 10
    assert rectangle(5, 4.5) == 22.5
    assert triangle(5, 2) == 5


def test_volume():
    assert cubic(3) == 27
    assert cubic(4) == 64
    assert cubic(1.7) == pytest.approx(4.912, .001)
    assert round(cubic(1.7), 2) == 4.91
    assert cylinder(1, 10) == 31.41592653589793
    assert cylinder(1, 10) == pytest.approx(31.4159, .0001)


