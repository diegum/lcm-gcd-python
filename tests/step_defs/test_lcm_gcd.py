# -*- coding: utf-8 -*-
"""
Prime factorization tests.
"""

# pylint: disable=C0103, C0116, W0621


from pytest_bdd import given, when, then, scenario

from ..context import maxmin


@scenario(
    '../features/lcm_gcd.feature',
    'LCM and GCD',
    example_converters=dict(a=int, b=int, lcm=int, gcd=int)
)
def test_lcm_gcd():
    pass


@given('<a> and <b> integers')
def pair_under_test(a, b):
    assert isinstance(a, int)
    assert isinstance(b, int)
    return dict(a=a, b=b)


@when('LCM & GCD are calculated')
def calculate_lcm_and_gcd(pair_under_test):
    pair_under_test['lcm'] = maxmin.lcm(pair_under_test['a'],
                                        pair_under_test['b'])
    pair_under_test['gcd'] = maxmin.gcd(pair_under_test['a'],
                                        pair_under_test['b'])


@then('they are respectively equivalent to <lcm> and <gcd>')
def check_lcm_and_gcd_to_equal_example(pair_under_test, lcm, gcd):
    assert lcm == pair_under_test['lcm']
    assert gcd == pair_under_test['gcd']
