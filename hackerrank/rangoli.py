"""
Rangoli Module

Prints the rangoli ascii art.
"""
from typing import List


BASE_CHAR = 96


def print_rangoli(size):
    lines = create_lines(size)
    print("\n".join(["".join(line) for line in lines]))


def create_lines(size: int):
    rows, cols, middle = get_dimensions(size)
    lines = []
    for i in get_change_positions_in_rows(middle, size):
        line_draw = ['-'] * cols
        add_characters(i, line_draw, middle)
        lines.append(line_draw)

    return lines


def get_dimensions(size: int):
    rows = size * 2 - 1
    cols = rows * 2 - 1
    middle = cols // 2 + 1
    return rows, cols, middle


def get_change_positions_in_rows(middle: int, size: int):
    offset = [i for i in range(size, 0, -1)] + [i for i in range(2, size + 1)]
    positions = [tuple(range(middle - i, middle + i + 1, 2)) for i in range(0, middle, 2)] + \
                [tuple(range(middle - i, middle + i + 1, 2))  for i in range(middle - 3, -1, -2)]
    return zip(positions, offset)


def add_characters(positions: List[tuple], line_draw: list, middle: int):
    line_columns, offset = positions
    for pos in line_columns:
        line_draw[pos - 1] = chr(BASE_CHAR + offset + abs(middle - pos) // 2)


if __name__ == '__main__':
    print_rangoli(int(input("Please type the size of the rangoli: ")))
