"""
Rangoli Module

Prints the rangoli ascii art.
"""

def get_dimensions(size):
	rows = size * 2 - 1
	cols = rows * 2 - 1
	middle = cols // 2 + 1
	return rows, cols, middle


def print_rangoli(size):
    rows = size * 2 - 1
    cols = rows * 2 - 1
    middle = cols // 2
    for i in range(rows):
        line = line[:middle - i] + chr(96 + size) * (i + 1) + line[middle + 1 + i:]
        print(line)
