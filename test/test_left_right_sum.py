def test_left_right_sum_1():
    array = [3, 4, 5, -2]
    assert left_right_sum(array) == 2


def test_left_right_sum_2():
    array = [10, 20, 30, -10]
    assert left_right_sum(array) == 2


def test_left_right_sum_3():
    array = [-1, -20, 10, -10]
    assert left_right_sum(array) == 1


def left_right_sum(array):
    n_sum = 0
    left = 0
    right = sum(array)
    for elem in array[:-1]:
        left += elem
        right -= elem
        if left > right:
            n_sum += 1

    return n_sum
