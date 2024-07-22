#!/usr/bin/python3
'''etermines if a given data set represents a valid UTF-8 encoding'''


def validUTF8(data):
    '''0. UTF-8 Validation'''
    is_valid_utf = False
    valid_utf = ["0", "110", "1110", "11110"]
    for decimal_data in data:
        binary_data = f'{decimal_data:08b}'
        x = binary_data[:1] == valid_utf[0]
        y = binary_data[:3] == valid_utf[1]
        z = binary_data[:4] == valid_utf[2]
        q = binary_data[:5] == valid_utf[3]
        is_valid_utf = x | y | z | q
    return is_valid_utf
