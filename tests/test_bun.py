import pytest
from ..bun import Bun
from ..data import BUN_TEST_DATA, COMMON_TEST_DATA

# Тест инициализации булочки и геттеров
@pytest.mark.parametrize("name, price", BUN_TEST_DATA)
def test_bun_init_and_getters(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price

# Тест инициализации булочки
def test_bun_init():
    name = "Test"
    price = 123.45
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price

# Тест метода get_name
def test_bun_get_name():
    name = COMMON_TEST_DATA['BUN_NAME']
    price = COMMON_TEST_DATA['BUN_PRICE']
    bun = Bun(name, price)
    assert bun.get_name() == name

# Тест метода get_price
def test_bun_get_price():
    name = COMMON_TEST_DATA['BUN_NAME']
    price = COMMON_TEST_DATA['BUN_PRICE']
    bun = Bun(name, price)
    assert bun.get_price() == price