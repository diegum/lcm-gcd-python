# -*- coding: utf-8 -*-
"""
Prime number tests.
"""

# pylint: disable=C0116, W0621


from pytest_bdd import given, when, then, scenario

from ..context import maxmin


@scenario(
    '../features/primes.feature',
    'Prime numbers',
    example_converters=dict(number=int)
)
def test_primes():
    pass


@given('a <number>')
def number_under_test(number):
    assert isinstance(number, int)
    return dict(number=number)


@when('checked for prime')
def check_for_prime(number_under_test):
    number_under_test['is_prime'] = maxmin.is_prime(number_under_test['number'])


@then('it passes')
def should_pass(number_under_test):
    assert number_under_test['is_prime'] is True


@scenario(
    '../features/primes.feature',
    'Composed numbers',
    example_converters=dict(number=int)
)
def test_composed():
    pass


@then('it doesn\'t pass')
def should_not_pass(number_under_test):
    assert number_under_test['is_prime'] is not True
