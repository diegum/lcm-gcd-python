# -*- coding: utf-8 -*-
"""LCM, GCD module."""


from typing import Generator


from math import ceil, sqrt


def is_prime(number: int) -> bool:
    """True if number is prime."""
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


def generate_primes_under(number: int) -> Generator[int, None, None]:
    """Yields primes under argument number."""
    abs_number = abs(number)
    iterator_number = 2
    while iterator_number < abs_number:
        if is_prime(iterator_number):
            yield iterator_number
        iterator_number += (1 if iterator_number == 2 else 2)
