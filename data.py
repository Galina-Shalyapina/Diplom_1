BURGER_PRICE_TEST_DATA = [
    ([('SAUCE', 'A', 10)], 50*2 + 10),
    ([('SAUCE', 'A', 10), ('FILLING', 'B', 20)], 50*2 + 10 + 20)
]

BUN_TEST_DATA = [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
]

INGREDIENT_TEST_DATA = [
    ('SAUCE', 'hot sauce', 100),
    ('FILLING', 'cutlet', 150),
]

COMMON_TEST_DATA = {
    'BUN_NAME': 'Test Bun',
    'BUN_PRICE': 50,
    'INGREDIENT_TYPE_SAUCE': 'SAUCE',
    'INGREDIENT_TYPE_FILLING': 'FILLING'
}