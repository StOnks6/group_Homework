from lib1 import get_affordable_products
from lib2 import END_PARTICLE, generate_tape


# For 1-st lib
def test_no_suitable_product():
    products = [{'product': 'bread', 'price': 25}, {'product': 'milk', 'price': 30}]
    max_price = 20
    assert get_affordable_products(products, max_price) == []


def test_everything_fits():
    products = [{'product': 'bread', 'price': 25}, {'product': 'milk', 'price': 30}]
    max_price = 40
    assert get_affordable_products(products, max_price) == ['bread', 'milk']


def test_part_fits_part_does_not():
    products = [{'product': 'bread', 'price': 25}, {'product': 'milk', 'price': 30}, {'product': 'eggs', 'price': 15}]
    max_price = 20
    assert get_affordable_products(products, max_price) == ['eggs']


# For 2-st lib
def test_generate_tape_standart_lenght():
    tape1 = generate_tape()
    assert tape1.endswith(END_PARTICLE)
    assert len(
        tape1) == 30  # 25 is amount of bytes of string which has lenght 20 digits (default length) + 5 (END_PARTICLE)


def test_generate_tape_specific_lenght():
    length = 10
    tape2 = generate_tape(length)
    assert tape2.endswith(END_PARTICLE)
    assert len(tape2) == length + 7
