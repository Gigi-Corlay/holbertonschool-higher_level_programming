#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    array_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i, common_symbol in enumerate(roman_string):
        if common_symbol not in array_values:
            return 0

        current_value = array_values[common_symbol]

        if i < len(roman_string) - 1:
            next_symbol = roman_string[i + 1]
            next_value = array_values[next_symbol]

            if current_value < next_value:
                total -= current_value
            else:
                total += current_value

        else:
            total += current_value

    return total
