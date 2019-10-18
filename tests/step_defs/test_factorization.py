# -*- coding: utf-8 -*-
"""
Prime factorization tests.
"""

# pylint: disable=C0116, W0621


from ast import literal_eval

from pytest_bdd import given, when, then, scenario

from ..context import maxmin


@scenario(
    '../features/prime_factorization.feature',
    'Prime factorization',
    example_converters=dict(number=int, prime_factors=str)
)
def test_factorization():
    pass


@given('a <number>')
def number_under_test(number):
    assert isinstance(number, int)
    return dict(number=number)


@when('submitted to prime factorization')
def generate_prime_factors(number_under_test):
    number_under_test['prime_factors'] = maxmin.generate_prime_factors(number_under_test['number'])


@then('it generates its <prime_factors>')
def generated_prime_factors(number_under_test, prime_factors):
    prime_list = literal_eval(prime_factors)
    index = 0
    prime_factor_generator = number_under_test['prime_factors']
    for factor in prime_factor_generator:
        assert index < len(prime_list), "Unexpected factors generated"
        assert factor == prime_list[index], "Generated factor different than expected"
        index += 1
    assert index == len(prime_list), "More prime factors expected"
