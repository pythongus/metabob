"""
Rangoli Module

Prints the rangoli ascii art.
"""
from typing import List


BASE_CHAR = 96


def get_dimensions(size: int):
    rows = size * 2 - 1
    cols = rows * 2 - 1
    middle = cols // 2 + 1
    return rows, cols, middle


def create_lines(size: int):
    rows, cols, middle = get_dimensions(size)
    lines = []
    for i in get_symmetrical_rows(middle, size):
        line_draw = ['-'] * cols
        add_chars(i, line_draw, middle)
        lines.append(line_draw)

    return lines


def add_chars(positions: List[tuple], line_draw: list, middle: int):
    line_columns, offset = positions
    for pos in line_columns:
        line_draw[pos - 1] = chr(BASE_CHAR + offset + abs(middle - pos) // 2)


def get_symmetrical_rows(middle: int, size: int):
    offset = [i for i in range(size, 0, -1)] + [i for i in range(2, size + 1)]
    positions = [tuple(range(middle - i, middle + i + 1, 2)) for i in range(0, middle, 2)] + \
                [tuple(range(middle - i, middle + i + 1, 2))  for i in range(middle - 3, -1, -2)]
    return zip(positions, offset)


def print_rangoli(size):
    lines = create_lines(size)
    print("\n".join(["".join(line) for line in lines]))
