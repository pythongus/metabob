"""
Unit tests for the hourglass sum algorithm.
"""
import math
import os
import random
import re
import sys
from hackerrank.two_d_arrays import (
        create_2d_array,
        hourglassSum,
	make_hour_glass,
        )


HG_1 = """
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
"""
HG_2 = """
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""
HG_3 = """
-9 -9 -9 1 1 1
0 -9 0 4 3 2
-9 -9 -9 1 2 3
0 0 8 6 6 0
0 0 0 -2 0 0
0 0 1 2 4 0
"""

def test_create_2d_array():
    arr = create_2d_array(HG_1)
    assert len(arr) == 6
    assert set([len(col) for col in arr]) == {6}
    assert arr[0][0] == 1
    assert arr[2][2] == 1
    assert arr[5][5] == 0


def test_create_third_2d_array():
    arr = create_2d_array(HG_3)
    assert len(arr) == 6
    assert set([len(col) for col in arr]) == {6}
    assert arr[0][0] == -9
    assert arr[5][2] == 3
    assert arr[5][5] == 0


def test_first_hourglass_sum():
    result = hourglassSum(create_2d_array(HG_1))
    assert result == 7


def test_second_hourglass_sum():
    result = hourglassSum(create_2d_array(HG_2))
    assert result == 19


def test_third_hourglass_sum():
    result = hourglassSum(create_2d_array(HG_3))
    assert result == 28


def test_make_hour_glass():
	arr = create_2d_array(HG_3)
	hg_arr = make_hour_glass(0, 0, arr)
	assert hg_arr == [-9, -9, -9, -9, -9, -9, -9]
