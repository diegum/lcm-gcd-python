# -*- coding: utf-8 -*-
"""LCM, GCD module."""

from math import ceil, sqrt
from typing import Generator, Union


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


def gcd(number_a: int, number_b: int) -> int:
    """Returns the greatest common divisor of its arguments."""
    result = 1

    a_factors = generate_prime_factors(number_a)
    b_factors = generate_prime_factors(number_b)

    a_factor = get_next_generated_value_or_none(a_factors)
    b_factor = get_next_generated_value_or_none(b_factors)

    while a_factor is not None and b_factor is not None:
        if a_factor == b_factor:
            result *= a_factor
            a_factor = get_next_generated_value_or_none(a_factors)
            b_factor = get_next_generated_value_or_none(b_factors)
        elif a_factor < b_factor:
            a_factor = get_next_generated_value_or_none(a_factors)
        else:
            b_factor = get_next_generated_value_or_none(b_factors)

    return result


def lcm(number_a: int, number_b: int) -> int:
    """Returns the least common multiple of its arguments."""
    result = 1

    a_factors = generate_prime_factors(number_a)
    b_factors = generate_prime_factors(number_b)

    a_factor = get_next_generated_value_or_none(a_factors)
    b_factor = get_next_generated_value_or_none(b_factors)

    while a_factor is not None or b_factor is not None:
        if a_factor is None:
            result *= b_factor
            b_factor = get_next_generated_value_or_none(b_factors)
        elif b_factor is None or a_factor < b_factor:
            result *= a_factor
            a_factor = get_next_generated_value_or_none(a_factors)
        elif b_factor < a_factor:
            result *= b_factor
            b_factor = get_next_generated_value_or_none(b_factors)
        else:
            result *= a_factor
            a_factor = get_next_generated_value_or_none(a_factors)
            b_factor = get_next_generated_value_or_none(b_factors)

    return result
