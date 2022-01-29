"""CSC111 Winter 2021 Assignment 1: Linked Lists, Part 1

Instructions (READ THIS FIRST!)
===============================

Please write your tests for Part 1 in this module. Make sure to review the assignment
instructions carefully for this part! You may find it helpful to consult this
section of the Course Notes:
https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html

While you must include unit tests, you may also use property-based tests in your test suite.

We will *not* be running PythonTA on this file; however, you should follow good programming
design and style in this file anyway, just like you would for all other work.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Isaac Waller.
"""
import pytest
from a1_part1 import MoveToFrontLinkedList, SwapLinkedList, CountLinkedList
from hypothesis import given
from hypothesis.strategies import integers

################################################################################
# Test cases for Heuristic 1
################################################################################

@given(x=integers())
def test_heuristic1_empty_list(x: int) -> None:
    """Test MoveToFrontLinkedList with an empty list when searching for any integer"""
    linky = MoveToFrontLinkedList([])
    assert linky.__contains__(x) == False


@given(x=integers())
def test_heuristic1_one_element_list(x: int) -> None:
    """Test MoveToFrontLinkedList with a list containing one element"""
    linky = MoveToFrontLinkedList([x])
    assert linky.__contains__(x) == True


@given(x=integers())
def test_heuristic1_one_element_list_mutation(x: int) -> None:
    """Test the mutation of a MoveToFrontLinkedList with a list containing one element"""
    linky = MoveToFrontLinkedList([x])
    linky.__contains__(x)
    assert linky.to_list() == [x]


def test_heuristic1_multiple_element_list_contains() -> None:
    """Test MoveToFrontLinkedList with a list containing multiple elements"""
    linky = MoveToFrontLinkedList(['a', 'b', 'c', 'd', 'e'])
    assert linky.__contains__('c') == True


def test_heuristic1_multiple_element_list_doesnt_contain() -> None:
    """Test MoveToFrontLinkedList with a list containing multiple elements"""
    linky = MoveToFrontLinkedList(['a', 'b', 'c', 'd', 'e'])
    assert linky.__contains__('Hello') == False


def test_heuristic1_multiple_element_list_mutation() -> None:
    """Test the mutation of a MoveToFrontLinkedList with a list containing multiple elements"""
    linky = MoveToFrontLinkedList(['a', 'b', 'c', 'd', 'e'])
    linky.__contains__('e')
    assert linky.to_list() == ['e', 'a', 'b', 'c', 'd']


def test_heuristic1_multiple_element_list_mutations() -> None:
    """Test multiple mutations of a MoveToFrontLinkedList with a list containing multiple elements"""
    linky = MoveToFrontLinkedList(['a', 'b', 'c', 'd', 'e'])
    linky.__contains__('e')
    linky.__contains__('a')
    linky.__contains__('b')
    linky.__contains__('Hello')
    assert linky.to_list() == ['b', 'a', 'e', 'c', 'd']

################################################################################
# Test cases for Heuristic 2
################################################################################

@given(x=integers())
def test_heuristic2_empty_list(x: int) -> None:
    """Test SwapLinkedList with an empty list when searching for any integer"""
    linky = SwapLinkedList([])
    assert linky.__contains__(x) == False


@given(x=integers())
def test_heuristic2_one_element_list(x: int) -> None:
    """Test SwapLinkedList with a list containing one element"""
    linky = SwapLinkedList([x])
    assert linky.__contains__(x) == True


@given(x=integers())
def test_heuristic2_one_element_list_mutation(x: int) -> None:
    """Test the mutation of a SwapLinkedList with a list containing one element"""
    linky = SwapLinkedList([x])
    linky.__contains__(x)
    assert linky.to_list() == [x]


@given(x=integers(), y=integers())
def test_heuristic2_two_element_list_mutation(x: int, y: int) -> None:
    """Test the mutation of a SwapLinkedList with a list containing two elements"""
    linky = SwapLinkedList([x, y])
    linky.__contains__(y)
    assert linky.to_list() == [y, x]


def test_heuristic2_multiple_element_list_contains() -> None:
    """Test SwapLinkedList with a list containing multiple elements"""
    linky = SwapLinkedList(['a', 'b', 'c', 'd', 'e'])
    assert linky.__contains__('c') == True


def test_heuristic2_multiple_element_list_doesnt_contain() -> None:
    """Test SwapLinkedList with a list containing multiple elements"""
    linky = SwapLinkedList(['a', 'b', 'c', 'd', 'e'])
    assert linky.__contains__('Hello') == False


def test_heuristic2_multiple_element_list_mutation() -> None:
    """Test the mutation of a SwapLinkedList with a list containing multiple elements"""
    linky = SwapLinkedList(['a', 'b', 'c', 'd', 'e'])
    linky.__contains__('d')
    assert linky.to_list() == ['a', 'b', 'd', 'c', 'e']


def test_heuristic2_multiple_element_list_mutations() -> None:
    """Test multiple mutations of a SwapLinkedList with a list containing multiple elements"""
    linky = SwapLinkedList(['a', 'b', 'c', 'd', 'e'])
    linky.__contains__('e')
    linky.__contains__('b')
    linky.__contains__('e')
    linky.__contains__('Hello')
    assert linky.to_list() == ['b', 'a', 'e', 'c', 'd']

################################################################################
# Test cases for Heuristic 3
################################################################################

@given(x=integers())
def test_heuristic3_empty_list(x: int) -> None:
    """Test CountLinkedList with an empty list when searching for any integer"""
    linky = CountLinkedList([])
    assert linky.__contains__(x) == False


@given(x=integers())
def test_heuristic3_one_element_list(x: int) -> None:
    """Test CountLinkedList with a list containing one element"""
    linky = CountLinkedList([x])
    assert linky.__contains__(x) == True


@given(x=integers())
def test_heuristic3_one_element_list_mutation(x: int) -> None:
    """Test the mutation of a CountLinkedList with a list containing one element"""
    linky = CountLinkedList([x])
    linky.__contains__(x)
    assert linky.to_list() == [x]


def test_heuristic3_multiple_element_list_contains() -> None:
    """Test CountLinkedList with a list containing multiple elements"""
    linky = CountLinkedList(['a', 'b', 'c', 'd', 'e'])
    assert linky.__contains__('c') == True


def test_heuristic3_multiple_element_list_doesnt_contain() -> None:
    """Test CountLinkedList with a list containing multiple elements"""
    linky = CountLinkedList(['a', 'b', 'c', 'd', 'e'])
    assert linky.__contains__('Hello') == False


def test_heuristic3_multiple_element_list_mutation() -> None:
    """Test the mutation of a CountLinkedList with a list containing multiple elements"""
    linky = CountLinkedList(['a', 'b', 'c', 'd', 'e'])
    linky.__contains__('e')
    assert linky.to_list() == ['e', 'a', 'b', 'c', 'd']


def test_heuristic3_multiple_element_list_mutations_simple_reorder() -> None:
    """Test multiple mutations of a CountLinkedList with a list containing multiple elements"""
    linky = CountLinkedList(['a', 'b', 'c', 'd', 'e'])
    linky.__contains__('e')
    linky.__contains__('a')
    linky.__contains__('b')
    linky.__contains__('Hello')
    assert linky.to_list() == ['e', 'a', 'b', 'c', 'd']


def test_heuristic3_multiple_element_list_mutations_complex_reorder() -> None:
    """Test multiple mutations of a CountLinkedList with a list containing multiple elements"""
    linky = CountLinkedList(['a', 'b', 'c', 'd', 'e'])
    linky.__contains__('e')
    for _ in range(0, 10):
        linky.__contains__('a')
    for _ in range (0, 5):
        linky.__contains__('b')
    for _ in range(0, 3):
        linky.__contains__('Hello')
    assert linky.to_list() == ['a', 'b', 'e', 'c', 'd']


if __name__ == '__main__':
    pytest.main(['a1_part1_test.py', '-v'])
