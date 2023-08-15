def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isupper() for c in password):
        return False

    special_characters = "+-/*!\"№;%:?*()="
    if not any(c in special_characters for c in password):
        return False

    if any(c.isspace() for c in password):
        return False

    if not all(c.isascii() for c in password):
        return False

    return True
