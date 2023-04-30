import pytest


@pytest.fixture
def menu_info():
   menus={'mocha': 40, 'latte': 50, 'espresso': 30}
   print(f'menus = {menus}')
   return menus

@pytest.fixture
def discount_value():
    return 10

def test_one(menu_info):
    assert menu_info['mocha']==40
    assert max(menu_info.values())==50

def test_two(menu_info):
    assert len(menu_info)==3
    assert sum(menu_info.values())==120
    assert sum(menu_info.values())/len(menu_info)==40

def test_three(menu_info, discount_value):
    assert menu_info['latte'] - discount_value == 40