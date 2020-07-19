"""
Unit Tests For Quick Sort Algorithm.
"""
import random
from hypothesis import given
import hypothesis.strategies as st
from hackerrank.quick_sort import quick_sort


def test_sort_empty_list():
    elements = quick_sort([])
    assert not elements


def test_sort_with_1_element():
    elements = quick_sort([1])
    assert elements == [1]


def test_sort_with_2_elements_1():
    elements = quick_sort([1, 2])
    assert elements == [1, 2]


def test_sort_with_2_elements_2():
    elements = quick_sort([2, 1])
    assert elements == [1, 2]


def test_sort_with_2_elements_3():
    elements = quick_sort([2, 2])
    assert elements == [2, 2]


def test_sort_with_3_elements_1():
    elements = quick_sort([1, 2, 3])
    assert elements == [1, 2, 3]


def test_sort_with_3_elements_2():
    elements = quick_sort([2, 1, 3])
    assert elements == [1, 2, 3]


def test_sort_with_3_elements_3():
    elements = quick_sort([2, 3, 1])
    assert elements == [1, 2, 3]


def test_sort_with_3_elements_4():
    elements = quick_sort([3, 2, 1])
    assert elements == [1, 2, 3]


@given(st.lists(st.integers()))
def test_sort_with_random_lists(xs):
    elements = list(xs)
    assert quick_sort(elements) == sorted(elements)