#!/usr/bin/python3
# filepath: /home/taylor/src/ProgrammingCliffnotes/Python3/test_examples.py

"""
Demonstrates testing frameworks and approaches in Python.
"""

from pytest import skip

def test_true():
    assert True

def test_false():
    assert (1+1==3)

def test_addition():
    assert (1+1==2)

def test_skip():
    skip() #This test will be skipped