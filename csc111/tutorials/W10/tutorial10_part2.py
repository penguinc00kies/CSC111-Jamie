"""CSC111 Tutorial 10: Recursive Sorting Algorithms

Module Description
==================
This file contains the start of the Timsort algorithm, which is used by Python
and other programming languages for their sorting functions.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu and Diane Horton.
"""


###############################################################################
# Task 1: Finding runs
###############################################################################
def find_runs(lst: list) -> list[tuple[int, int]]:
    """Return a list of tuples indexing the runs of lst.

    Preconditions:
        - lst != []

    >>> find_runs([0, 1, 2, 3, 4, 5])
    [(0, 6)]
    >>> find_runs([10, 4, -2, 1])
    [(0, 1), (1, 2), (2, 4)]
    >>> find_runs([1, 4, 7, 10, 2, 5, 3, -1])
    [(0, 4), (4, 6), (6, 7), (7, 8)]
    """
    runs = []

    # Keep track of the start and end points of the current run.
    run_start = 0
    run_end = 1

    while run_end < len(lst):
        # Loop invariant:
        # - is_sorted(lst[run_start:run_end])

        # How can you tell if a run should continue?
        #   (When you do, update run_end.)

        # How can you tell if a run is over?
        #   (When you do, update runs, run_start, and run_end.)
        if lst[run_end - 1] <= lst[run_end]:
            # print(str(lst[run_start]) + ' ' + str(lst[run_end]) )
            run_end += 1
            if run_end == len(lst):
                runs.append((run_start, run_end))
        else:
            runs.append((run_start, run_end))
            run_start = run_end
            run_end = run_end + 1
    if run_end == len(lst) and (len(runs) == 0 or runs[-1] != (run_start, run_end)):
        runs.append((run_start, run_end))

    return runs



###############################################################################
# Task 2: Merging runs
###############################################################################
def timsort1(lst: list) -> None:
    """Sort the given list.

    This algorithm works by first finding all runs in lst, and then repeatedly
    merging consecutive runs until there's only one run left---the entire list.

    >>> lst = []
    >>> timsort1(lst)
    >>> lst
    []
    >>> lst = [1]
    >>> timsort1(lst)
    >>> lst
    [1]
    >>> lst = [1, 4, 7, 10, 2, 5, 3, -1]
    >>> timsort1(lst)
    >>> lst
    [-1, 1, 2, 3, 4, 5, 7, 10]
    """
    runs = find_runs(lst)

    # Treat runs as a stack and repeatedly merge the top two runs
    # When the loop ends, the only run should be the whole list.
    # HINT: see the merge_sublists functions below.
    runs = find_runs(lst)

    while len(runs) > 1:
        last = runs.pop()
        second_last = runs.pop()
        merge_sublists(lst, second_last[0], second_last[1], last[1])
        runs.append((second_last[0], last[1]))


def merge_sublists(lst: list, b: int, m: int, e: int) -> None:
    """Merge two sorted sublists in lst into one sorted sublist.

    This was an exercise from Prep 10. You can copy-and-paste your implementation from the prep!
    """
    start = lst[:b]
    lst1 = lst[b:m]
    lst2 = lst[m:e]
    end = lst[e:]
    i1, i2 = 0, 0
    sorted_so_far = []

    while i1 < m - b and i2 < e - m:
        # Loop invariant:
        # sorted_so_far is a merged version of lst1[:i1] and lst2[:i2]
        assert sorted_so_far == sorted(lst1[:i1] + lst2[:i2])

        if lst1[i1] <= lst2[i2]:
            sorted_so_far.append(lst1[i1])
            i1 += 1
        else:
            sorted_so_far.append(lst2[i2])
            i2 += 1

    # When the loop is over, either i1 == len(lst1) or i2 == len(lst2)
    assert i1 == m - b or i2 == e - m

    # In either case, the remaining unmerged elements can be concatenated to sorted_so_far.
    if i1 == m - b:
        temp = start + sorted_so_far + lst2[i2:] + end
    else:
        temp = start + sorted_so_far + lst1[i1:] + end

    for i in range(len(temp)):
        lst[i] = temp[i]


###############################################################################
# Task 3: Limiting the "runs" stack
###############################################################################
def timsort2(lst: list) -> None:
    """Sort lst in place.

    This function works by finding runs and merging them incrementally, using
    the algorithm described on the assignment handout.
    """
    # Initialize a list of runs.
    runs = []

    run_start = 0
    run_end = 1
    # repeat until the runs cover the entire list
    while run_end < len(lst):
        # Find the next run and add it to the list
        while lst[run_end-1] <= lst[run_end]:
            run_end += 1
        runs.append((run_start, run_end))

        if len(runs) >= 3:
            # Check the properties B > C and A > B + C, and merge until they are satisfied
            A = length_of_run(runs[-3])
            B = length_of_run(runs[-2])
            C = length_of_run(runs[-1])
            while not(B > C and A > B + C):
                c = runs.pop()
                b = runs.pop()
                a = runs.pop()
                if B <= C:
                    merge_sublists(lst, b[0], b[1], c[1])
                    runs.append(a)
                    runs.append((b[0], c[1]))
                if A <= B + C:
                    if A < C:
                        merge_sublists(lst, a[0], a[1], b[1])

    # Merge all remaining runs
    while ...:
        ...


def length_of_run(run: tuple[int, int]) -> int:
    """return"""
    return run[1] - run[0]


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'disable': ['E1136']
    # }