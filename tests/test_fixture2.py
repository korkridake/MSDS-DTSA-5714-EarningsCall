import pytest
from mlib import fmt_name, gen_email


@pytest.fixture
def input_values():
    return ('Peter', 'Parker')


def test_one(input_values):
    assert fmt_name('tony', 'stark') == 'Tony STARK'
    assert fmt_name(input_values[0], input_values[1]) == 'Peter PARKER'


def test_two(input_values):
    assert gen_email(input_values[0], input_values[1],
                     'marvel.com') == 'peter.p@marvel.com'
