"""CSC111 Tutorial 10: Recursive Sorting Algorithms

Module Description
==================
This module contains the start of a small program that can visualize sorting algorithms,
similar to the one from Tutorial 9. You can also find the in-place implementation of
quicksort from lecture this week; that's what you'll be visualizing in this exercise.

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

import pygame
from pygame.colordict import THECOLORS


TIME_PER_FRAME = 20  # Number of milliseconds per frame in the animation


################################################################################
# In-place quicksort
################################################################################
def in_place_quicksort(lst: list) -> None:
    """Sort the given list using the quicksort algorithm.
    """
    _in_place_quicksort(lst, 0, len(lst))


def _in_place_quicksort(lst: list, b: int, e: int) -> None:
    """Sort the sublist lst[b:e] using the quicksort algorithm.

    Preconditions:
        - 0 <= b <= e <= len(lst)
    """
    if e - b < 2:
        # Do nothing; lst[b:e] is already sorted
        pass
    else:
        # Partition lst[b:e]
        pivot_index = _in_place_partition(lst, b, e)

        # Recursively sort each partition
        _in_place_quicksort(lst, b, pivot_index)
        _in_place_quicksort(lst, pivot_index + 1, e)


def _in_place_partition(lst: list[int], b: int, e: int) -> int:
    """Mutate lst so that lst[b:e] is partitioned with pivot lst[b].

    Return the *new index of the pivot*.

    Preconditions:
        - 0 <= b < e <= len(lst)
    """
    pivot = lst[b]
    small_i = b + 1
    big_i = e

    while small_i < big_i:
        # Loop invariants
        # assert all(lst[j] <= pivot for j in range(b + 1, small_i))
        # assert all(lst[j] > pivot for j in range(big_i, e))

        if lst[small_i] <= pivot:
            small_i += 1
        else:
            lst[small_i], lst[big_i - 1] = lst[big_i - 1], lst[small_i]
            big_i -= 1

    # Move the pivot to between the "smaller" and "bigger" parts
    lst[b], lst[small_i - 1] = lst[small_i - 1], lst[b]

    # Return the index of the pivot
    return small_i - 1


################################################################################
# Tutorial exercises
################################################################################
class Visualizer:
    """A class responsible for visualizing a sorting algorithm.
    """
    # Private Instance Attributes:
    #   - _screen: The pygame screen to draw on.
    #   - row: The current row number to draw a list on. (Increases every time
    #          self.draw_list is called.)
    _screen: pygame.Surface
    _row: int

    def __init__(self, screen_size: tuple[int, int]) -> None:
        """Initialize a new visualizer that has a screen with the given size.

        Preconditions:
            - screen_size[0] > 0 and screen_size[1] > 0
        """
        self._screen = initialize_screen(screen_size)
        self._row = 0

    def draw_list(self, lst: list[int]) -> None:
        """Render lst as a grid row in this visualizer's screen.

        Instead of using a row parameter, use self._row to determine the row number to draw
        the list in. For example, if self._row = 0, the list is drawn at the top of the screen,
        and if self._row = len(lst) - 1, the list is drawn at the bottom of the screen.
        After drawing the row, INCREASE self._row by 1.

        Use the Surface.get_width, Surface.get_height, and/or Surface.get_size methods to
        determine the size of the screen, so that you can calculate the grid cell dimensions.

        Each integer is converted to a greyscale colour for the visualization.

        Preconditions:
            - all(0 <= n <= 255 for n in lst)
            - lst != []
            - 0 <= row < len(lst)
        """
        cell_width = self._screen.get_width() / len(lst)
        cell_height = self._screen.get_height() / len(lst)


        # Update pygame display (don't change this, and keep it at the end of the function body)
        pygame.display.flip()


def visualize_quicksort(lst: list[int], screen_size: tuple[int, int]) -> None:
    """Visualize quicksort on the given list of integers using pygame.

    Preconditions:
        - all(0 <= n <= 255 for n in lst)
        - lst != []
        - screen_size[0] >= len(lst) and screen_size[1] >= len(lst)

    Implementation notes:
        - We've called initialize_screen to obtain a pygame screen for you
          (you just need to pass it to draw_list).
        - Remember that your code should look very similar to in_place_quicksort,
          except with additional calls to draw_list.

          NOTE: You won't be able to close the pygame window while the animation is in
          progress, only after it's done. But you can still stop the Python interpreter
          altogether by clicking the red square button in PyCharm.
    """
    visualizer = Visualizer(screen_size)
    visualizer.draw_list(lst)

    # TODO: Add code here
    ...

    # Don't remove this! (See function docstring for details)
    wait_for_quit()


def _visualize_quicksort(visualizer: Visualizer, lst: list[int], b: int, e: int) -> None:
    """Visualize running in-place quicksort on lst[b:e].

    This visualization draws a new row for every iteration in the "partition" helper.

    Preconditions:
        - all(0 <= n <= 255 for n in lst)
        - 0 <= b <= e <= len(lst)
    """


def _visualize_partition(visualizer: Visualizer, lst: list[int], b: int, e: int) -> int:
    """Mutate lst so that lst[b:e] is partitioned with pivot lst[b].

    Return the *new index of the pivot*.
    Also, visualize each iteration of the loop using the given visualizer, and
    visualize the list after the pivot has been swapped to its correct location.

    Preconditions:
        - 0 <= b < e <= len(lst)
        - all(0 <= n <= 255 for n in lst)

    Implementation notes:
        - Call pygame.time.wait to animate the algorithm (drawing one row at a time);
          we've provided a constant that you can use, but feel free to experiment with
          other values as well.
          See https://www.pygame.org/docs/ref/time.html for details.

          NOTE: You won't be able to close the pygame window while the animation is in
          progress, only after it's done. But you can still stop the Python interpreter
          altogether by clicking the red square button in PyCharm.

    """


################################################################################
# Pygame helper functions (you can safely ignore these)
################################################################################
def initialize_screen(screen_size: tuple[int, int]) -> pygame.Surface:
    """Initialize pygame and the display window.

    This is a helper function for the "visualize_graph" functions above.
    You can safely ignore this function.
    """
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill(THECOLORS['white'])
    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.QUIT])

    return screen


def wait_for_quit() -> None:
    """Wait until user closes the pygame window.

    Preconditions:
        - pygame window has been opened
    """
    while True:
        if any(event.type == pygame.QUIT for event in pygame.event.get()):
            break
    pygame.display.quit()
    pygame.quit()


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