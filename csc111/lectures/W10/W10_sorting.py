"""CSC111 W10 - Starter File (Recursive Sorting)

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.
"""
from typing import Any


###################################################################################################
# Demo
###################################################################################################
def quicksort(lst: list) -> list:
    """Return a sorted list with the same elements as lst.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.

    >>> quicksort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst.copy()
    else:
        # 1. Divide the list into two parts
        pivot = lst[0]
        smaller, bigger = _partition(lst[1:], pivot)

        # 2. Sort each part recursively
        small_sorted = quicksort(smaller)
        big_sorted = quicksort(bigger)

        # 3. Combine the sorted parts
        return small_sorted + [pivot] + big_sorted


def _partition(lst: list, pivot: Any) -> tuple[list, list]:
    """Return a partition of lst with the chosen pivot.

    Return two lists, where the first contains the items in lst
    that are <= pivot, and the second contains the items in lst that are > pivot.
    """
    smaller = []
    bigger = []

    for item in lst:
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)

    return smaller, bigger


###################################################################################################
# Exercise 1 - Question 2
###################################################################################################
def _in_place_partition(lst: list) -> None:
    """Mutate lst so that it is partitioned with pivot lst[0].

    Let pivot = lst[0]. The elements of lst are moved around so that lst looks like

        [x1, x2, ... x_m, pivot, y1, y2, ... y_n],

    where each of the x's is <= pivot, and each of the y's is > pivot.

    >>> example_list = [10, 3, 20, 5, 16, 30, 7, 100]
    >>> _in_place_partition(example_list)  # pivot is 10
    >>> example_list[3]  # the 10 is now at index 3
    10
    >>> set(example_list[:3]) == {3, 5, 7}
    True
    >>> set(example_list[4:]) == {16, 20, 30, 100}
    True
    """
    pivot = lst[0]
    small_i = 1
    big_i = len(lst)

    while small_i != big_i:
        # Loop invariants
        assert all(item <= pivot for item in lst[:small_i])
        assert all(item > pivot for item in lst[big_i:])
        if lst[small_i] <= pivot:
            small_i += 1
        else:
            big_i -= 1
            lst[small_i], lst[big_i] = lst[big_i], lst[small_i]

    assert small_i == big_i
    lst[0], lst[big_i-1] = lst[big_i-1], lst[0]


################################################################################
# Exercise 1 - Question 3
################################################################################
def in_place_quicksort(lst: list) -> None:
    """Sort the given list using the quicksort algorithm."""


def _in_place_quicksort(lst: list, b: int, e: int) -> None:
    """Sort the given list[b: e using the quicksort algorithm.

    Preconditions:
        - 0 <= b <= e <= len(lst)
    """
    if b - e < 2:
        pass
    else:
        pivot_index = _in_place_partition_extra(lst, b, e)

        _in_place_quicksort(lst, b, pivot_index)
        _in_place_quicksort(lst, pivot_index + 1, e)


def _in_place_partition_extra(lst: list, b: int, e: int) -> int:
    """Mutate lst[b:e] so that it is partitioned with pivot lst[b].

    Also, return the new index of the pivot
    """
    pivot = lst[b]
    small_i = b + 1
    big_i = e

    while small_i != big_i:
        # Loop invariants
        assert all(item <= pivot for item in lst[b + 1:small_i])
        assert all(item > pivot for item in lst[big_i: e])
        if lst[small_i] <= pivot:
            small_i += 1
        else:
            big_i -= 1
            lst[small_i], lst[big_i] = lst[big_i], lst[small_i]

    assert small_i == big_i
    lst[b], lst[big_i-1] = lst[big_i-1], lst[b]
    return big_i - 1