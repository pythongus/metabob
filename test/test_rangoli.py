"""
Unit Tests for Rangoli Algorithm.
"""
from hackerrank.rangoli import (
    create_lines,
    get_change_positions_in_rows,
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


def test_get_change_positions_in_rows_size_5():
    size = 5
    _, _, middle = get_dimensions(size)
    assert list(get_change_positions_in_rows(middle, size))[0] == ((9,), 5)


def test_get_change_positions_in_rows_size_4():
    size = 4
    _, _, middle = get_dimensions(size)
    assert list(get_change_positions_in_rows(middle, size))[0] == ((7,), 4)


def test_add_chars():
    pass
