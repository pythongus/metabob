"""
Rangoli Module

Prints the rangoli ascii art.
"""


BASE_CHAR = 96


def get_dimensions(size):
    rows = size * 2 - 1
    cols = rows * 2 - 1
    middle = cols // 2 + 1
    return rows, cols, middle


def create_lines(size):
    rows, cols, middle = get_dimensions(size)
    lines = []
    for i in get_symmetrical_rows(size):
        line_draw = ['-'] * cols
        for j in range(cols):
            add_chars(i, j, middle, size, line_draw)

        lines.append(line_draw)

    return lines


def add_chars(i, j, middle, size, line_draw):
   for k in range(size):
       if j == middle - (3 + 2 * k) or j == middle + (1 + 2 * k):
           offset = BASE_CHAR + i + 1 + k
           if offset <= BASE_CHAR + size:
               line_draw[j] = chr(offset)
       elif j == middle - 1:
           offset = BASE_CHAR + i
           line_draw[j] = chr(offset)


def get_symmetrical_rows(size):
    return [i for i in range(size, 0, -1)] + [i for i in range(2, size + 1)] 


def print_rangoli(size):
    lines = create_lines(size)
    print("\n".join(["".join(line) for line in lines]))
