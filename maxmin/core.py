# -*- coding: utf-8 -*-
"""LCM, GCD module."""

from typing import Generator, Union

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


def get_next_generated_value_or_none(generator: Generator[int, None, None]) -> Union[int, None]:
    """
    Returns the next element of an argument generator, or None, if a StopIteration exception arose.
    """
    try:
        return next(generator)
    except StopIteration:
        pass


def generate_prime_factors(number: int) -> Generator[int, None, None]:
    """Yields ascending or equal prime factors that compose the argument number."""
    abs_number = abs(number)
    primes = generate_primes_under(number + 1)

    last_prime = get_next_generated_value_or_none(primes)
    if last_prime is not None:
        while abs_number != 1:
            if abs_number % last_prime == 0:
                yield last_prime
                abs_number = int(abs_number / last_prime)
            else:
                last_prime = get_next_generated_value_or_none(primes)
