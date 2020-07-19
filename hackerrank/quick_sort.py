"""
Classic Quick Sort Algorithm
"""


def quick_sort(elements: list):
    """Sorts the elements in the given list using the
    quick sort algorithm.
    """
    qsort(elements, 0, len(elements) - 1)
    return elements


def qsort(elems:list, lo: int, hi: int):
    """Executes the recursive call to the partitions"""
    if lo < hi:
        pi = partition(elems, lo, hi)
        qsort(elems, lo, pi - 1)
        qsort(elems, pi + 1, hi)


def partition(elems, lo, hi) -> int:
    """Sorts the elements in the partition given by lo(w) and
    hi(gh) ends.
    """
    i = lo - 1
    pivot = elems[hi]
    for j in range(lo, hi):
        if elems[j] < pivot:
            i += 1
            swap(elems, i, j)

    swap(elems, i + 1, hi)
    return i + 1


def swap(elems: list, first: int, second: int):
    """Swaps the position of two elements"""
    elems[first], elems[second] = elems[second], elems[first]
