"""
2D arrays module.

For Hackerrank tests.
"""


def create_2d_array(source: str):
    arr = zip(*[[int(cell) for cell in row.split(' ')] for row in source.split('\n') if row])
    return list(arr)


def hourglassSum(arr):
    """Complete the hourglassSum function below."""
    hg_arr = [make_hour_glass(i, j, arr) for i in range(4) for j in range(4)]
    return max([sum(array) for array in hg_arr])


def make_hour_glass(i: int, j: int, arr: list):

    def in_hour_glass(x: int, y:int):
        return not((x == 0 and y == 1) or (x == 2 and y == 1))

    return [arr[x + i][y + j] for x in range(3) for y in range(3) if in_hour_glass(x, y)]
