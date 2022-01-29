"""CSC111 Winter 2021 Assignment 1: Linked Lists, Part 1

Instructions (READ THIS FIRST!)
===============================

This Python module contains three linked list subclasses corresponding to the three
moving heuristics described on the assignment handout.

You need to complete their implementations by overriding the __contains__ method
(and only for CountLinkedList, additional methods as required).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Isaac Waller.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional

from a1_linked_list import LinkedList, _Node


################################################################################
# Heuristic 1 (move to front)
################################################################################
class MoveToFrontLinkedList(LinkedList):
    """A linked list implementation that uses a "move to front" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique
    """
    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, move it to the front of this list.

        >>> linky = MoveToFrontLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [40, 10, 20, 30, 50, 60]
        """
        curr = self._first
        prev = None

        while not (curr is None or curr.item == item):
            prev = curr
            curr = curr.next

        if curr is None:
            return False
        else:
            if prev is None:
                return True

            prev.next = curr.next
            curr.next = self._first
            self._first = curr
            return True



################################################################################
# Heuristic 2 (swap)
################################################################################
class SwapLinkedList(LinkedList):
    """A linked list implementation that uses a "swap" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique
    """
    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, swap it with the item before it, if any.
        You may do this by reassigning _Node item or next attributes (or both).

        >>> linky = SwapLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [10, 20, 40, 30, 50, 60]
        """
        curr = self._first
        prev = None
        prevprev = None

        while not (curr is None or curr.item == item):
            prevprev = prev
            prev = curr
            curr = curr.next

        if curr is None:
            return False
        else:
            if prev is None:
                return True
            if prevprev is None:
                prev.next = curr.next
                curr.next = prev
                self._first = curr
                return True

            found_item = curr
            prevprev.next = found_item
            prev.next = found_item.next
            found_item.next = prev
            return True


################################################################################
# Heuristic 3 (count)
################################################################################
# NOTE: this heuristic requires a new kind of _Node that has an additional "count" attribute.
@dataclass
class _CountNode(_Node):
    """A node in a CountLinkedList.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
      - access_count: The number of times this node has been accessed (used by the count heuristic)
    """
    next: Optional[_CountNode] = None
    access_count: int = 0


class CountLinkedList(LinkedList):
    """A linked list implementation that uses a "swap" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique
        - nodes are sorted in non-increasing order by access_count

    NOTE: In order to make use of the _CountNode class above, you'll need to override every
    LinkedList method in a1_linked_list.py that creates new _Node objects to create _CountNode
    objects instead. Your code for the overridden methods should be otherwise identical.
    """
    _first: Optional[_CountNode]

    def append(self, item: Any) -> None:
        """Add the given item to the end of this linked list.
        """
        new_node = _CountNode(item)

        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, increase its count and reorder the nodes in
        non-increasing count order---see assignment handout for details.

        >>> linky = CountLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [40, 10, 20, 30, 50, 60]
        """
        curr = self._first
        prev = None

        while not (curr is None or curr.item == item):
            prev = curr
            curr = curr.next

        if curr is None:
            return False
        else:
            curr.access_count += 1
            if prev is None:
                return True

            prev.next = curr.next

            found_item = curr
            curr = self._first
            prev = None

            while curr.access_count >= found_item.access_count:
                prev = curr
                curr = curr.next

            if prev is None:
                found_item.next = self._first
                self._first = found_item
                return True

            prev.next = found_item
            found_item.next = curr
            return True

# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'max-line-length': 100,
#         'disable': ['E1136'],
#         'extra-imports': ['a1_linked_list'],
#         'max-nested-blocks': 4
#     })
#
#     import python_ta.contracts
#     python_ta.contracts.check_all_contracts()
#
#     import doctest
#     doctest.testmod()
