import pytest
from ..ingredient import Ingredient
from ..data import INGREDIENT_TEST_DATA, COMMON_TEST_DATA

# Тест инициализации ингредиента
@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_ingredient_init(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.type == ingredient_type
    assert ingredient.name == name
    assert ingredient.price == price

# Тест метода get_type
@pytest.mark.parametrize("ingredient_type", [COMMON_TEST_DATA['INGREDIENT_TYPE_SAUCE'], COMMON_TEST_DATA['INGREDIENT_TYPE_FILLING']])
def test_ingredient_get_type(ingredient_type):
    ingredient = Ingredient(ingredient_type, "Test", 10)
    assert ingredient.get_type() == ingredient_type

# Тест метода get_name
def test_ingredient_get_name():
    name = "TestSauce"
    ingredient = Ingredient(COMMON_TEST_DATA['INGREDIENT_TYPE_SAUCE'], name, 10)
    assert ingredient.get_name() == name

# Тест метода get_price
def test_ingredient_get_price():
    price = 42
    ingredient = Ingredient(COMMON_TEST_DATA['INGREDIENT_TYPE_FILLING'], "TestFilling", price)
    assert ingredient.get_price() == price