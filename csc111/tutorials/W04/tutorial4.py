"""CSC111 Tutorial 4: Trees, Trees, Trees

Module Description
==================
This module contains the Tree class we developed in this week's lectures, as well as
various methods and functions for you to implement as part of today's tutorial.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu and Diane Horton.
"""
from __future__ import annotations

import csv
import random
from typing import Any, Optional


class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and RecursiveList; the only major
    difference is that _rest has been replaced by _subtrees to handle multiple
    recursive sub-parts.

    Representation Invariants:
        - self._root is not None or self._subtrees == []
        - all(not subtree.is_empty() for subtree in self._subtrees)
    """
    # Private Instance Attributes:
    #   - _root:
    #       The item stored at this tree's root, or None if the tree is empty.
    #   - _subtrees:
    #       The list of subtrees of this tree. This attribute is empty when
    #       self._root is None (representing an empty tree). However, this attribute
    #       may be empty when self._root is not None, which represents a tree consisting
    #       of just one item.
    _root: Optional[Any]
    _subtrees: list[Tree]

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If root is None, the tree is empty.

        Preconditions:
            - root is not none or subtrees == []
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of items contained in this tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        """
        if self.is_empty():
            return 0
        else:
            size = 1  # count the root
            for subtree in self._subtrees:
                size += subtree.__len__()  # could also write len(subtree)
            return size

    def __contains__(self, item: Any) -> bool:
        """Return whether the given is in this tree.

        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> t.__contains__(1)
        True
        >>> t.__contains__(5)
        True
        >>> t.__contains__(4)
        False
        """
        if self.is_empty():
            return False
        elif self._root == item:
            return True
        else:
            for subtree in self._subtrees:
                if subtree.__contains__(item):
                    return True
            return False

    def __str__(self) -> str:
        """Return a string representation of this tree.

        For each node, its item is printed before any of its
        descendants' items. The output is nicely indented.

        You may find this method helpful for debugging.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + f'{self._root}\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is
                # modified.
                s += subtree._str_indented(depth + 1)
            return s

    def remove(self, item: Any) -> bool:
        """Delete *one* occurrence of the given item from this tree.

        Do nothing if the item is not in this tree.
        Return whether the given item was deleted.
        """
        if self.is_empty():
            return False
        elif self._root == item:
            self._delete_root()  # delete the root
            return True
        else:
            for subtree in self._subtrees:
                deleted = subtree.remove(item)
                if deleted and subtree.is_empty():
                    # The item was deleted and the subtree is now empty.
                    # We should remove the subtree from the list of subtrees.
                    # Note that mutate a list while looping through it is
                    # EXTREMELY DANGEROUS!
                    # We are only doing it because we return immediately
                    # afterwards, and so no more loop iterations occur.
                    self._subtrees.remove(subtree)
                    return True
                elif deleted:
                    # The item was deleted, and the subtree is not empty.
                    return True

            # If the loop doesn't return early, the item was not deleted from
            # any of the subtrees. In this case, the item does not appear
            # in this tree.
            return False

    def _delete_root(self) -> None:
        """Remove the root item of this tree.

        Preconditions:
            - not self.is_empty()
        """
        if self._subtrees == []:
            self._root = None
        else:
            # Strategy: Promote a subtree (the rightmost one is chosen here).
            # Get the last subtree in this tree.
            last_subtree = self._subtrees.pop()

            self._root = last_subtree._root
            self._subtrees.extend(last_subtree._subtrees)

    ############################################################################
    # Tutorial Part 1: Tree insertion
    ############################################################################
    def insert(self, item: Any) -> None:
        """Insert the given item into this tree using the following algorithm.

        1. If the tree is empty, make item the new root of the tree.
        2. If the tree has a root but no subtrees, create a new subtree of this tree that
           contains the item.
        3. Otherwise, pick a random number between 1 and 3 inclusive.
            - If the random number is 3, create a new subtree of this tree that contains
              the item.
            - If the random number is a 1 or 2, pick one of the existing
              subtrees at random, and *recursively insert* the new item
              into that subtree.

        This exercise is meant to help you review the random module.
        You'll find these two functions helpful:

            - random.randint
            - random.choice

        >>> t = Tree(None, [])
        >>> t.insert(1)
        >>> 1 in t
        True
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.insert(100)
        >>> t.__contains__(100)
        True
        >>> t = Tree(1, [lt, rt])
        >>> t.insert(100)
        >>> t.__contains__(100)
        True
        """
        if self.is_empty():
            self._root = item
        elif self._subtrees == []:
            new_tree = Tree(item, [])
        else:
            number = random.randint(1, 3)
            if number == 3:
                new_tree = Tree(item, [])
                self._subtrees.append(new_tree)
            else:
                number = random.randint(1, len(self._subtrees) - 1)
                self._subtrees[number].insert(item)


    def insert_sequence(self, items: list) -> None:
        """Insert the given items into this tree.

        The inserted items form a chain of descendants, where:
            - items[0] is a child of this tree's root
            - items[1] is a child of items[0]
            - items[2] is a child of items[1]
            - etc.

        Do nothing if items is empty.

        Do not create duplicate items that share the same parent; for example, if items[0] is
        already a child of this tree's root, you should recurse into that existing subtree rather
        than create a new subtree with items[0].
        But if items[0] is not a child of this tree's root, create a new subtree for it
        and append it to the existing list of subtrees.

        Hint: to do this recursively, you'll need to recurse on both the tree argument
        (from self to a subtree) AND on the given items, using the "first" and "rest" idea
        from RecursiveLists. To access the "rest" of a built-in Python list, you can use
        list slicing: items[1:len(items)], or simply items[1:].

        Preconditions:
            - not self.is_empty()

        >>> t = Tree(111, [])
        >>> t.insert_sequence([1, 2, 3])
        >>> print(t)
        111
          1
            2
              3
        <BLANKLINE>
        >>> t.insert_sequence([1, 3, 5])
        >>> print(t)
        111
          1
            2
              3
            3
              5
        <BLANKLINE>
        """
        if items != []:
            if items[0] == self._root:
                for subtree in self._subtrees:
                    subtree.insert_sequence(items)
            if items[0] != self._root:
                new_tree = Tree(items[0], [])
                self._subtrees.append(new_tree)

            self.insert_sequence(items[1:])


            # target_subtree = None
            # for subtree in self._subtrees:
            #     if items[0] == self._root:
            #         target_subtree = subtree
            #         break
            #
            # if target_subtree is None:
            #     target_subtree = Tree(items[0], [])
            #     self._subtrees.append(target_subtree)
            #
            # target_subtree.insert_sequence(items[1:])


################################################################################
# Tutorial Part 3: Decision trees
################################################################################
def build_decision_tree(file: str) -> Tree:
    """Build a decision tree storing the animal data from the given file.

    Preconditions:
        - file is the path to a csv file in the format of the provided animals.csv
    """
    tree = Tree('', [])  # The start of a decision tree

    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip the header row

        for row in reader:
            # row is a list[str] containing the data in the file.
            # Your task is to process this list so that you can insert it into tree.
            ...

    return tree


ANIMAL_QUESTIONS = [
    'Does this animal have hair?',
    'Does this animal lay eggs?',
    'Is this animal aquatic?',
    'Is this animal a predator?',
    'Does this animal have exactly 4 legs?',
    'Does this animal have a tail?',
    'Is this animal a mammal?'
]


def get_user_input(questions: list[str]) -> list[bool]:
    """Return the user's answers to a list of Yes/No questions."""
    answers_so_far = []

    for question in questions:
        print(question)
        s = input('Y/N: ')
        answers_so_far.append(s == 'Y')  # Any other input is interpreted as False

    return answers_so_far


def run_animal_guesser(animal_file: str) -> None:
    """Run an animal guessing program based on the given animal data file.

    This function should:
        1. Create a decision tree based on the given animal file.
        2. Prompt the user for their desired animal characteristics.
        3. Traverse the decision tree to determine the possible animals(s) that match
           the user's inputs. You will likely need to implement a new Tree method to
           accomplish this part.
        4. Print the results back to the user. This might be "no animals", an exact match
           (one animal), or multiple animals. You can choose the exact messages you print.
    """


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    # import doctest
    # doctest.testmod()

    # import python_ta
    # python_ta.check_all('tutorial4.py', config={
    #     'max-line-length': 100,
    #     'extra-imports': ['csv', 'random'],
    #     'disable': ['E1136'],
    #     'allowed-io': ['build_decision_tree', 'get_user_input', 'run_animal_guesser']
    # })