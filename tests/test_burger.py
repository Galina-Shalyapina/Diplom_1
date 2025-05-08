import pytest

from ..burger import Burger
from ..data import BURGER_PRICE_TEST_DATA, COMMON_TEST_DATA


# Тест расчета цены бургера
@pytest.mark.parametrize("ingredients, expected_price", BURGER_PRICE_TEST_DATA)
def test_burger_price(bun_mock, ingredient_mock, ingredients, expected_price):
    burger = Burger()

    # Устанавливаем булочку
    burger.set_buns(bun_mock())

    # Добавляем ингредиенты
    for type_, name, price in ingredients:
        burger.add_ingredient(ingredient_mock(type_, name, price))

    assert burger.get_price() == expected_price


# Тест добавления, удаления и перемещения ингредиентов
def test_burger_add_remove_move_ingredient(bun_mock, ingredient_mock):
    burger = Burger()

    # Устанавливаем булочку
    burger.set_buns(bun_mock())

    # Создаем ингредиенты
    ing1 = ingredient_mock("SAUCE", "A", 10)
    ing2 = ingredient_mock("FILLING", "B", 20)
    ing3 = ingredient_mock("FILLING", "C", 30)

    # Добавляем ингредиенты
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.add_ingredient(ing3)

    # Перемещаем ингредиент
    burger.move_ingredient(2, 0)
    assert burger.ingredients[0] == ing3

    # Удаляем ингредиент
    burger.remove_ingredient(1)
    assert len(burger.ingredients) == 2


# Тест генерации чека
def test_burger_receipt(bun_mock, ingredient_mock):
    burger = Burger()

    # Устанавливаем булочку
    burger.set_buns(bun_mock())

    # Создаем ингредиент
    ingredient = ingredient_mock("SAUCE", "A", 10)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert COMMON_TEST_DATA['BUN_NAME'] in receipt
    assert "a A" in receipt or "A" in receipt
    assert f"Price: {COMMON_TEST_DATA['BUN_PRICE'] * 2 + 10}" in receipt