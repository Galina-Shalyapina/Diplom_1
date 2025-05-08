import pytest
from unittest.mock import Mock

@pytest.fixture
def bun_mock():
    """Создает мок-булочку с заданными параметрами"""
    def _create_bun(name="Test Bun", price=50):
        mock_bun = Mock()
        mock_bun.get_price.return_value = price
        mock_bun.get_name.return_value = name
        return mock_bun
    return _create_bun

@pytest.fixture
def ingredient_mock():
    """Создает мок-ингредиент с заданными параметрами"""
    def _create_ingredient(type_="SAUCE", name="Test Ingredient", price=10):
        mock_ing = Mock()
        mock_ing.get_price.return_value = price
        mock_ing.get_name.return_value = name
        mock_ing.get_type.return_value = type_
        return mock_ing
    return _create_ingredient
