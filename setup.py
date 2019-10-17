# -*- coding: utf-8 -*-
"""Module setup metadata."""

from setuptools import setup, find_packages


with open('README.rst') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='max-min',
    version='0.1.0',
    description='Sample app to calculate LCM & GCD',
    long_description=README,
    author='Diego Dagum',
    author_email='diego@diegodagum.com',
    url='https://github.com/diegum/max-min',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
