"""CSC111 Winter 2022 Prep 2: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains the implementation of linked lists we studied in lecture
last week, including the append method and updated initializer from the prep reading.

There are two additional methods at the bottom of the class that we have started.
Your first task is to implement EACH method based on the method header and description.

Your second task is to write a set of tests for each of the methods, as described at the bottom
of this file. This is good review of how to write unit tests in Python from CSC110, which you'll
need to do throughout this course.

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.

You do not need to add additional doctests. However, you should test your work carefully
before submitting it!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr and David Liu.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional

import pytest  # You'll need to use pytest.raises in your tests (see below)


@dataclass
class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
    """
    item: Any
    next: Optional[_Node] = None  # By default, this node does not link to any other node


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]

    def __init__(self, items: Iterable) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        for item in items:
            self.append(item)

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list.

        The items in this linked list appear in the same order in the returned list.
        """
        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

    def append(self, item: Any) -> None:
        """Append item to the end of this list.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.append(4)
        >>> lst.to_list()
        [1, 2, 3, 4]
        """
        new_node = _Node(item)

        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node

    ############################################################################
    # Prep exercises start here
    ############################################################################
    def remove_first(self) -> Any:
        """Remove and return the first element of this list.

        Raise an IndexError if this list is empty.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove_first()
        1
        >>> lst.to_list()
        [2, 3]
        >>> lst.remove_first()
        2
        >>> lst.remove_first()
        3
        """
        if self._first is None:
            raise IndexError

        first = self._first.item
        self._first = self._first.next
        return first

    def remove_last(self) -> Any:
        """Remove and return the last element of this list.

        Raise an IndexError if this list is empty.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove_last()
        3
        >>> lst.to_list()
        [1, 2]
        >>> lst.remove_last()
        2
        >>> lst.remove_last()
        1

        IMPLEMENTATION HINTS:
            1. You'll need to modify the linked list traversal pattern to reach
               the *second-last node*.
            2. It's okay to have separate cases (using if statements) for size-0
               and size-1 linked lists.
        """
        if self._first is None:
            raise IndexError

        if self._first.next is None:
            last = self._first.item
            self._first = None
            return last

        curr = self._first

        while curr.next.next is not None:
            curr = curr.next

        last = curr.next.item
        curr.next = None
        return last


################################################################################
# Test cases
################################################################################
# Write unit tests for each of the two LinkedList methods you implemented above.
# Your tests should cover various cases for possible linked list lengths, and
# should check both for mutation and the correct return value.
# You can use the LinkedList.to_list method to check the values in the linked list.
# Each unit test should have a docstring containing a brief description of the test.
#
# To review how to write unit tests using pytest (including testing for errors being raised),
# please consult
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html.
#
# WARNING: your test function names MUST start with "test_", otherwise they won't
# be detected as unit tests by pytest, and therefore won't be run.

def test_remove_first_when_empty() -> None:
    """Test remove_first when given an empty linked list"""
    linky = LinkedList([])
    with pytest.raises(IndexError):
        linky.remove_first()


def test_remove_first_when_one_item() -> None:
    """Test remove_first when given a linked list with one item"""
    linky = LinkedList([1])
    assert linky.remove_first() == 1
    with pytest.raises(IndexError):
        linky.remove_first()


def test_remove_first_eight_items() -> None:
    """Test remove_first when given a linked list with eight items"""
    linky = LinkedList([8, 7, 6, 5, 4, 3, 2, 1])
    for i in range(8, 0, -1):
        assert linky.remove_first() == i
    with pytest.raises(IndexError):
        linky.remove_first()


def test_remove_last_when_empty() -> None:
    """Test remove_last when given an empty linked list"""
    linky = LinkedList([])
    with pytest.raises(IndexError):
        linky.remove_last()


def test_remove_last_one_item() -> None:
    """Test remove_first when given a linked list with one item"""
    linky = LinkedList([1])
    assert linky.remove_last() == 1
    with pytest.raises(IndexError):
        linky.remove_first()


def test_remove_last_eight_items() -> None:
    """Test remove_last when given a linked list with eight items"""
    linky = LinkedList([8, 7, 6, 5, 4, 3, 2, 1])
    for i in range(1, 9):
        assert linky.remove_last() == i
    with pytest.raises(IndexError):
        linky.remove_first()


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136']
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    pytest.main(['prep2.py', '-v'])
