#!/usr/bin/python3

def roman_to_int(roman_string):
    result = 0
    if roman_string is not None and isinstance(roman_string, str):
        std = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        strlen = len(roman_string)
        for i in range(strlen):
            if i > 0 and std[roman_string[i]] > std[roman_string[i - 1]]:
                result += std[roman_string[i]] - 2 * std[roman_string[i - 1]]
            else:
                result += std[roman_string[i]]
    return result

