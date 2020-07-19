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
    for index in range(1, len(array)):
        if sum(array[:index]) > sum(array[index:]):
            n_sum += 1

    return n_sum
