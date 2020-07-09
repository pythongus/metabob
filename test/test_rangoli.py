"""
Unit Tests for Rangoli Algorithm.
"""
from hackerrank.rangoli import (
    create_lines,
    get_symmetrical_rows,
    get_dimensions,
    )


def test_create_with_5_lines():
    size = 5
    lines = create_lines(size)
    print()
    print("\n".join(["".join(line) for line in lines]))
    assert "".join(lines[0]) == '--------e--------'
    assert "".join(lines[1]) == '------e-d-e------'
    assert "".join(lines[2]) == '----e-d-c-d-e----'
    assert "".join(lines[3]) == '--e-d-c-b-c-d-e--'
    assert "".join(lines[4]) == 'e-d-c-b-a-b-c-d-e'
    assert "".join(lines[5]) == '--e-d-c-b-c-d-e--'


def test_create_with_6_lines():
    size = 6
    lines = create_lines(size)
    print()
    print("\n".join(["".join(line) for line in lines]))
    assert "".join(lines[0]) == '----------f----------'
    assert "".join(lines[1]) == '--------f-e-f--------'
    assert "".join(lines[2]) == '------f-e-d-e-f------'
    assert "".join(lines[3]) == '----f-e-d-c-d-e-f----'
    assert "".join(lines[4]) == '--f-e-d-c-b-c-d-e-f--'
    assert "".join(lines[5]) == 'f-e-d-c-b-a-b-c-d-e-f'
    assert "".join(lines[6]) == '--f-e-d-c-b-c-d-e-f--'


def test_get_symmetrical_rows_size_5():
    _, _, middle = get_dimensions(5)
    assert get_symmetrical_rows(middle) == [(9,), (7, 9, 11), (5, 7, 9, 11, 13), (3, 5, 7, 9, 11, 13, 15),
                                            (1, 3, 5, 7, 9, 11, 13, 15, 17), (3, 5, 7, 9, 11, 13, 15),
                                            (5, 7, 9, 11, 13), (7, 9, 11), (9,)]


def test_get_symmetrical_rows_size_4():
    _, _, middle = get_dimensions(4)
    assert get_symmetrical_rows(middle) == [(7,), (5, 7, 9), (3, 5, 7, 9, 11), (1, 3, 5, 7, 9, 11, 13),
                                            (3, 5, 7, 9, 11), (5, 7, 9), (7,)]


def test_add_chars():
    pass
