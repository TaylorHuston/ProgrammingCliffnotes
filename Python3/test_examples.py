#!/usr/bin/python3

"""
Demonstrates testing frameworks and approaches in Python.
"""

from pytest import skip


def test_true():
    assert True


def test_false():
    assert (1+1 == 3)


def test_addition():
    assert (1+1 == 2)


def test_skip():
    skip()  # This test will be skipped
