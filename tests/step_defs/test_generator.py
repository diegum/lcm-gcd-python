# -*- coding: utf-8 -*-
"""
Prime generator tests.
"""


# pylint: disable=C0116, W0621


from ast import literal_eval
from pytest_bdd import given, when, then, scenario


from ..context import maxmin


@scenario(
    '../features/prime_generator.feature',
    'Prime generation',
    example_converters=dict(number=int, primes=str)
)
def test_generator():
    pass


@given('a <number>')
def number_under_test(number):
    assert isinstance(number, int)
    return dict(number=number)


@when('submitted to prime generation')
def generate_primes(number_under_test):
    number_under_test['primes'] = maxmin.generate_primes_under(number_under_test['number'])


@then('it generates <primes> under it')
def generated_primes(number_under_test, primes):
    prime_list = literal_eval(primes)
    index = 0
    prime_generator = number_under_test['primes']
    for prime in prime_generator:
        assert index < len(prime_list), "Unexpected primes generated"
        assert prime == prime_list[index], "Generated prime different than expected"
        index += 1
    assert index == len(prime_list), "More primes expected"
