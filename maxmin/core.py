# -*- coding: utf-8 -*-
"""LCM, GCD module"""


from math import ceil, sqrt


def is_prime(number: int) -> bool:
    """True if number is prime"""
    abs_number = abs(number)

    if abs_number == 1:
        return False
    if abs_number == 2:
        return True

    if abs_number % 2 == 0:
        return False

    for divisor in range(3, ceil(sqrt(abs_number)) + 1, 2):
        if abs_number % divisor == 0:
            return False

    return True
