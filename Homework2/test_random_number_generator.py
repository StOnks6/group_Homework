
from random_number_generator import generate_random_number

def test_generated_number_range():
    generated_number = generate_random_number()
    assert 0 <= generated_number <= 1000, "Generated number is not in the required range"
