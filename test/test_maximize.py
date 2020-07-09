from functools import lru_cache


def test_1():
    resp = maximize(1000,
                    [[25, 16],
                     [49, 64, 81],
                     [25, 49, 64, 81, 100],
                     ])
    assert resp == 206


def maximize(m, sets):

    def _calc(elem, set_, accum):
        for set_elem in set_:
            accum.append(elem + set_elem)
        return accum

    def calc(elems, set_, accum):
        for elem in elems:
            accum = _calc(elem, set_, accum)
        return accum

    def calculate(elems, sets, accum):
        if not sets and not accum:
            return elems
        elif not elems or not sets:
            return accum
        accum = calc(elems, sets[0], accum)
        return calculate(accum, sets[1:], [])

    nums = calculate(sets[0], sets[1:], [])
    return max([num % m for num in nums])
