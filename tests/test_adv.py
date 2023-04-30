from area import rectangle, triangle
from volume import *
from hero import *
import pytest


def test_list():
    assert cubic(2)==8
    assert cubic(3)==27
    assert cubic(4)==64
    assert cubic(5)==125

    assert [cubic(n) for n in range(2, 6)] == [8, 27, 64, 125]
    assert [cubic(n) for n in [5, 10, 20]] == [125, 1000, 8000]

    assert rectangle(1, 2)==2
    assert rectangle(5, 3)==15
    assert [rectangle(w, h) for w, h in [(1, 2), [5, 3]]] == [2, 15]

def test_dict():
    assert hero('black widow') == {'fname': 'Natasha', 'lname': 'Romanoff'}

def test_exception():
    with pytest.raises(ValueError):
        rectangle(-5, 2)

    assert rectangle(5, 2)==10

    with pytest.raises(ValueError, match=r'w, h must be greater than zero.'):
        rectangle(-5, 2)

    # with pytest.raises(FileExistsError):
    #     rectangle(-5, 2)
