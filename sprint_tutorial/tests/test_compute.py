""" Tests for the compute module
"""
from nose.tools import assert_equal

from sprint_tutorial.compute import my_sum
from sprint_tutorial.compute import my_subtract


def test_my_sum1():
    assert_equal(my_sum(0, 0), 0)


def test_my_sum2():
    assert_equal(my_sum(1, -1), 0)

def test_my_subtract1():
    assert_equal(my_subtract(2, 1), 1)

def test_my_subtract2():
    assert_equal(my_subtract(5, 3), 2)
