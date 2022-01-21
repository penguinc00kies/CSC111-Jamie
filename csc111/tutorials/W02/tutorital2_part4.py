"""CSC111 Tutorial 2: More with Linked Lists, Part 4

Module Description
==================
This module contains the code for a *doubly-linked list* implementation.
Note the similarities and differences between the classes in this file
and the equivalent _Node and LinkedList class from lecture.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional


@dataclass
class _DoubleNode:
    """A node in a doubly-linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the DoublyLinkedList class, but not by client code.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
      - prev: The previous node in the list, if any.

    Representation Invariants:
      - # Translate this to Python: this node is the "prev" of its "next" node
    """
    item: Any
    prev: Optional[_DoubleNode] = None  # By default, this node does not link to any other node
    next: Optional[_DoubleNode] = None  # By default, this node does not link to any other node


class DoublyLinkedList:
    """A doubly-linked list implementation of the List ADT.

    Representation Invariants:
        - self._first is None == self._last is None
    """
    # Private Instance Attributes:
    #   - _first: The first node in the linked list, or None if the list is empty.
    #   - _last: The last node in the linked list, or None if the list is empty.
    #   - _length: The size of the linked list.
    _first: Optional[_DoubleNode]
    _last: Optional[_DoubleNode]
    _length: int

    def __init__(self, items: Iterable) -> None:
        """Initialize a new doubly-linked list containing the given items.
        """
        items = list(items)
        self._length = len(items)
        self._last = _DoubleNode(items[len(items)-1])

        curr = self._last
        for i in range(len(items)-2, -1, -1):
            new_node = _DoubleNode(items[i])
            new_node.next = curr
            curr.prev = new_node
            curr = new_node
        self._first = curr