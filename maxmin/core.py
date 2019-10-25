# -*- coding: utf-8 -*-
"""LCM, GCD module."""

from math import ceil, sqrt
from typing import Dict, Generator, List, Tuple, Union


class Global:
    """
    If not specified, exported functions of this module will default the
    application of dynamic programming to this constant.
    """
    DYNAMIC_DEFAULT: bool = True

    """
    In the optimized version, all primes generated are kept here.
    """
    generated_primes: List[int] = []

    """
    In the optimized version, this dictionary keeps previously obtained
    factorizations.
    """
    prime_factorizations: Dict[int, Tuple[int, int]] = {}

    """
    In the optimized version, this dictionary keeps previously obtained
    factorizations.
    """
    last_generate_primes_under_input_param: int = 0

    @staticmethod
    def dummy_1() -> None:
        """Just avoiding lint R0903(too-few-public-methods)"""

    @staticmethod
    def dummy_2() -> None:
        """Just avoiding lint R0903(too-few-public-methods)"""


def is_prime(number: int) -> bool:
    """True if number is prime."""
    abs_number = abs(number)

    if abs_number == 2:
        return True
    if abs_number == 1 or abs_number % 2 == 0:
        return False

    for divisor in range(3, ceil(sqrt(abs_number)) + 1, 2):
        if abs_number % divisor == 0:
            return False

    return True


def generate_primes_under(number: int, dynamic=Global.DYNAMIC_DEFAULT) -> \
        Generator[int, None, None]:
    """Yields primes under argument number."""
    return generate_primes__optimized(number) \
        if dynamic else generate_primes__non_optimized(number)


def generate_primes__optimized(number: int) -> Generator[int, None, None]:
    """Yields primes under argument number."""
    abs_number = abs(number)
    generated_primes = Global.generated_primes

    for prime in generated_primes:
        if prime >= abs_number:
            break
        yield prime

    while Global.last_generate_primes_under_input_param < abs_number:
        param_to_test = Global.last_generate_primes_under_input_param
        Global.last_generate_primes_under_input_param += 1
        if is_prime(param_to_test):
            generated_primes.append(param_to_test)
            yield param_to_test


def generate_primes__non_optimized(number: int) -> \
        Generator[int, None, None]:
    """Yields primes under argument number."""
    abs_number = abs(number)
    iterator_number = 2
    while iterator_number < abs_number:
        if is_prime(iterator_number):
            yield iterator_number
        iterator_number += (1 if iterator_number == 2 else 2)


def get_next_generated_value_or_none(generator: Generator[int, None, None]) \
        -> Union[int, None]:
    """
    Returns the next element of an argument generator, or None, if a
    StopIteration exception arose.
    """
    try:
        return next(generator)
    except StopIteration:
        pass


def generate_prime_factors(number: int, dynamic=Global.DYNAMIC_DEFAULT) -> \
        Generator[int, None, None]:
    """
    Yields ascending or equal prime factors that compose the argument number.
    """
    return generate_prime_factors__optimized(number) \
        if dynamic else generate_prime_factors__non_optimized(number)


def generate_prime_factors__optimized(number: int) -> \
        Generator[int, None, None]:
    """
    Yields ascending or equal prime factors that compose the argument number.
    This version is optimized, in the sense that no prime factorization will be
    calculated twice. After the first time calculated, the result is reused.
    For example, if we decompose 28 in its prime factors and then we try to
    decompose 14, the partial result got while decomposing 28 (2 x 14) is
    returned.
    """
    abs_number = abs(number)
    prime_factorizations = Global.prime_factorizations
    primes = generate_primes__optimized(abs_number + 1)
    last_prime = get_next_generated_value_or_none(primes)
    while last_prime is not None and abs_number != 1:
        if abs_number in prime_factorizations:
            (prime, abs_number) = prime_factorizations[abs_number]
            yield prime
        else:
            if abs_number % last_prime == 0:
                prime_factorizations[abs_number] = \
                    (last_prime, int(abs_number / last_prime))
            else:
                last_prime = get_next_generated_value_or_none(primes)


def generate_prime_factors__non_optimized(number: int) -> \
        Generator[int, None, None]:
    """
    Yields ascending or equal prime factors that compose the argument number.
    """
    abs_number = abs(number)
    primes = generate_primes__non_optimized(abs_number + 1)

    last_prime = get_next_generated_value_or_none(primes)
    while last_prime is not None and abs_number != 1:
        if abs_number % last_prime == 0:
            yield last_prime
            abs_number = int(abs_number / last_prime)
        else:
            last_prime = get_next_generated_value_or_none(primes)


def gcd(number_a: int, number_b: int, dynamic=Global.DYNAMIC_DEFAULT) -> int:
    """Returns the greatest common divisor of its arguments."""
    result = 1

    a_factors = generate_prime_factors(number_a, dynamic)
    b_factors = generate_prime_factors(number_b, dynamic)

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


def lcm(number_a: int, number_b: int, dynamic=Global.DYNAMIC_DEFAULT) -> int:
    """Returns the least common multiple of its arguments."""
    result = 1

    a_factors = generate_prime_factors(number_a, dynamic)
    b_factors = generate_prime_factors(number_b, dynamic)

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
