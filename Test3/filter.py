def is_valid_number(value):
    return isinstance(value, (int)) and value > 500

some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600,358]

filtered_data = list(filter(is_valid_number, some_data))
