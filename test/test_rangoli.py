"""
Unit Tests for Rangoli Algorithm.
"""
from hackerrank.rangoli import get_dimensions


BASE_CHAR = 96


def test_create_line():
    size = 5
    lines = create_line(size)
    print()
    print("\n".join(["".join(line) for line in lines]))
    assert "".join(lines[0]) == '--------e--------'
    assert "".join(lines[1]) == '------e-d-e------'
    assert "".join(lines[2]) == '----e-d-c-d-e----'
    assert "".join(lines[3]) == '--e-d-c-b-c-d-e--'
    assert "".join(lines[4]) == 'e-d-c-b-a-b-c-d-e'
    assert "".join(lines[5]) == '--e-d-c-b-c-d-e--'


def test_get_symmetrical_rows_size_5():
    size = 5
    assert get_symmetrical_rows(size) == [5, 4, 3, 2, 1, 2, 3, 4, 5]


def test_get_symmetrical_rows_size_4():
    size = 4
    assert get_symmetrical_rows(size) == [4, 3, 2, 1, 2, 3, 4]


def create_line(size):
    rows, cols, middle = get_dimensions(size)
    lines = []
    for i in get_symmetrical_rows(size):
        line_draw = ['-'] * cols
        for j in range(cols):
            if j == middle - 1:
                offset = BASE_CHAR + i
                line_draw[j] = chr(offset)
            elif size - i > 0:
                for k in range(size - 1):
                    if j == middle - (3 + 2 * k) or j == middle + (1 + 2 * k):
                        offset = BASE_CHAR + i + 1 + k
                        if offset <= BASE_CHAR + size:
                            line_draw[j] = chr(offset)
        lines.append(line_draw) 
    
    return lines 


def get_symmetrical_rows(size):
    return [i for i in range(size, 0, -1)] + [i for i in range(2, size + 1)] 
