"""
Unit Tests for Rangoli Algorithm.
"""
from hackerrank.rangoli import get_dimensions

class TestDimensions:

    def test_get_dimensions_for_size_1(self):
        size = 1
        rows, cols, middle = get_dimensions(size)
        assert rows == 1
        assert cols == 1
        assert middle == 1

    def test_get_dimensions_for_size_5(self):
        size = 5
        rows, cols, middle = get_dimensions(size)
        assert rows == 9
        assert cols == 17
        assert middle == 9


    def test_get_dimensions_for_size_10(self):
        size = 10
        rows, cols, middle = get_dimensions(size)
        assert rows == 19
        assert cols == 37
        assert middle == 19


    def test_get_dimensions_for_size_2(self):
        size = 2
        rows, cols, middle = get_dimensions(size)
        assert rows == 3
        assert cols == 5
        assert middle == 3
