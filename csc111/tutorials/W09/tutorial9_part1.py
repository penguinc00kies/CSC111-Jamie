"""CSC111 Tutorial 9: Iterative Sorting Algorithms

Module Description
==================
This module contains the selection sort and insertion sort implementations we studied
in lecture, and new exercises for you to complete in Part 1 of this tutorial.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu.
"""


def is_sorted(lst: list) -> bool:
    """Return whether lst is sorted.

    Formally, a list `lst` is sorted when for every index i between 0 and len(lst),
    lst[i] <= lst[i + 1]. Note that empty lists and lists of length 1 are always sorted.

    Do not call `sorted` or `list.sort` here.

    >>> is_sorted([2, 7, 3, 4, 5])
    False
    """
    return all(lst[i] <= lst[i + 1] for i in range(0, len(lst) - 1))


################################################################################
# Selection sort
################################################################################
def selection_sort(lst: list) -> None:
    """Sort the given list using the selection sort algorithm.

    Note that this is a *mutating* function.

    >>> lst = [3, 7, 2, 5]
    >>> selection_sort(lst)
    >>> lst
    [2, 3, 5, 7]
    """
    for i in range(0, len(lst)):
        # Loop invariants
        assert is_sorted(lst[:i])
        assert i == 0 or all(lst[i - 1] <= lst[j] for j in range(i, len(lst)))

        # Find the index of the smallest item in lst[i:] and swap that
        # item with the item at index i.
        index_of_smallest = _min_index(lst, i)
        lst[index_of_smallest], lst[i] = lst[i], lst[index_of_smallest]


def _min_index(lst: list, i: int) -> int:
    """Return the index of the smallest item in lst[i:].

    In the case of ties, return the smaller index (i.e., the index that appears first).

    Preconditions:
        - 0 <= i <= len(lst) - 1

    >>> _min_index([2, 7, 3, 5], 1)
    2
    """
    index_of_smallest_so_far = i

    for j in range(i + 1, len(lst)):
        if lst[j] < lst[index_of_smallest_so_far]:
            index_of_smallest_so_far = j

    return index_of_smallest_so_far


# Version that returns a new list
def selection_sort_simple(lst: list) -> list:
    """Return a sorted version of lst.

    The current implementation is actually techincally incorrect, as it mutates lst.
    We could fix this by first making a copy of lst and then operating on that copy.

    >>> selection_sort_simple([5, 3, 10, 7])
    [3, 5, 7, 10]
    """
    sorted_so_far = []

    # lst = lst.copy()
    while lst != []:
        smallest = min(lst)
        lst.remove(smallest)
        sorted_so_far.append(smallest)

    return sorted_so_far


################################################################################
# Insertion sort
################################################################################
def insertion_sort(lst: list) -> None:
    """Sort the given list using the selection sort algorithm.

    Note that this is a *mutating* function.

    >>> lst = [7, 3, 5, 2]
    >>> insertion_sort(lst)
    >>> lst
    [2, 3, 5, 7]
    """
    for i in range(0, len(lst)):
        # Loop invariant
        assert is_sorted(lst[:i])
        _insert(lst, i)


def _insert(lst: list, i: int) -> None:
    """Move lst[i] so that lst[:i + 1] is sorted.

    Preconditions:
        - 0 <= i < len(lst)
        - is_sorted(lst[:i])

    >>> lst = [7, 3, 5, 2]
    >>> _insert(lst, 1)
    >>> lst
    [3, 7, 5, 2]
    """
    # Version 1, using an early return
    # for j in range(i, 0, -1):  # This goes from i down to 1
    #     if lst[j - 1] <= lst[j]:
    #         return
    #     else:
    #         # Swap lst[j - 1] and lst[j]
    #         lst[j - 1], lst[j] = lst[j], lst[j - 1]

    # Version 2, using a compound loop condition
    j = i
    while not (j == 0 or lst[j - 1] <= lst[j]):
        # Swap lst[j - 1] and lst[j]
        lst[j - 1], lst[j] = lst[j], lst[j - 1]

        j -= 1


################################################################################
# Tutorial exercises
################################################################################
def selection_sort_rev(lst: list) -> None:
    """An in-place version of selection sort that builds up the sorted list from right-to-left.

    So after i iterations, the items in lst[len(lst) - i:] are sorted. Note that the list should
    still be sorted in non-decreasing order, so lst[len(lst) - i:] will contain the i LARGEST
    elements in lst.

    Implementation notes:
        - It is possible to complete this function with a loop variable that starts at 0 and
          counts up, or that starts at len(lst) (or len(lst) - 1) and counts down.
        - Translate the loop invariants as well!

    >>> lst = [3, 7, 2, 5]
    >>> selection_sort_rev(lst)
    >>> lst
    [2, 3, 5, 7]
    """
    for i in range(len(lst) - 1, -1, -1):
        assert is_sorted(lst[i:])
        assert i == 0 or all(lst[i] <= lst[j] for j in range(i, len(lst)))

        index_of_largest = _max_index(lst, i)
        lst[index_of_largest], lst[i] = lst[i], lst[index_of_largest]


def _max_index(lst: list, i: int) -> int:
    """Return the index of the largest item in lst[:i].

    In the case of ties, return the smaller index (i.e., the index that appears first).

    Preconditions:
        - 0 <= i <= len(lst) - 1

    >>> _max_index([2, 7, 3, 5], 1)
    2
    """
    index_of_largest_so_far = 0

    for j in range(0, i + 1):
        if lst[j] > lst[index_of_largest_so_far]:
            index_of_largest_so_far = j

    return index_of_largest_so_far


def insertion_sort_rev(lst: list) -> None:
    """An in-place version of insertion sort that builds up the sorted list from right-to-left.

    So after i iterations, the items in lst[len(lst) - i:] are sorted.

    Implementation notes:
        - It is possible to complete this function with a loop variable that starts at 0 and
          counts up, or that starts at len(lst) (or len(lst) - 1) and counts down.
        - Translate the loop invariants as well!
    >>> lst = [7, 3, 5, 2]
    >>> insertion_sort_rev(lst)
    >>> lst
    [2, 3, 5, 7]
    """
    for i in range(len(lst) - 1, 0, -1):
        # Loop invariant
        assert is_sorted(lst[i:])
        _insert_rev(lst, i)


def _insert_rev(lst: list, i: int) -> None:
    """Move lst[i] so that lst[i:] is sorted.

    Preconditions:
        - 0 <= i < len(lst)
        - is_sorted(lst[i:])

    >>> lst = [7, 3, 5, 2]
    >>> _insert(lst, 1)
    >>> lst
    [3, 7, 5, 2]
    """
    while i != len(lst) and lst[i] < lst[i - 1]:
        lst[i], lst[i - 1] = lst[i - 1], lst[i]
        i = i + 1


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'disable': ['E1136']
    # })