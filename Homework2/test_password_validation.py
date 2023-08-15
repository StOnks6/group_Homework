
from password_validation import is_valid_password

def test_valid_password():
    assert is_valid_password("StrongPass123!"), "Valid password not recognized"

def test_invalid_password_length():
    assert not is_valid_password("Short1!"), "Invalid password length not detected"

def test_invalid_password_no_digits():
    assert not is_valid_password("OnlyLetters!"), "Invalid password without digits not detected"

