"""CSC111 Tutorial 9: Iterative Sorting Algorithms

Module Description
==================
This module contains the start of a small program that can visualize sorting algorithms
(or more generally, lists of numbers).

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
from typing import Callable, Optional

import pygame
from pygame.colordict import THECOLORS


def selection_sort_key(lst: list, key: Optional[Callable] = None) -> None:
    """Sort the given list using the selection sort algorithm.

    If key is not None, sort the items by their corresponding return value when passed to key.

    Note that this is a *mutating* function.

    >>> lst = ['cat', 'octopus', 'hi', 'david']
    >>> selection_sort_key(lst, key=len)
    >>> lst
    ['hi', 'cat', 'david', 'octopus']
    >>> lst2 = ['cat', 'octopus', 'hi', 'david']
    >>> insertion_sort_key(lst2)
    >>> lst2
    ['cat', 'david', 'hi', 'octopus']
    """
    for i in range(0, len(lst)):
        index_of_smallest = _min_index_key(lst, i, key)
        lst[index_of_smallest], lst[i] = lst[i], lst[index_of_smallest]


def _min_index_key(lst: list, i: int, key: Optional[Callable] = None) -> int:
    """Return the index of the smallest item in lst[i:].

    If key is not None, rank items based on their return value when passed to key.
    In the case of ties, return the smaller index (i.e., the index that appears first).

    Preconditions:
        - 0 <= i <= len(lst) - 1

    >>> _min_index_key(['hi', 'octopus', 'cat', 'david'], 1, key=len)
    2
    """
    index_of_smallest_so_far = i

    for j in range(i + 1, len(lst)):
        if key is None:
            if lst[j] < lst[index_of_smallest_so_far]:
                index_of_smallest_so_far = j
        else:
            if key(lst[j]) < key(lst[index_of_smallest_so_far]):
                index_of_smallest_so_far = j

    return index_of_smallest_so_far


def insertion_sort_key(lst: list, key: Optional[Callable] = None) -> None:
    """Sort the given list using the selection sort algorithm.

    If key is not None, sort the items by their corresponding return value when passed to key.

    Note that this is a *mutating* function.

    >>> lst = ['octopus', 'cat', 'david', 'hi']
    >>> insertion_sort_key(lst, key=len)
    >>> lst
    ['hi', 'cat', 'david', 'octopus']
    >>> lst2 = ['octopus', 'cat', 'david', 'hi']
    >>> insertion_sort_key(lst2)
    >>> lst2
    ['cat', 'david', 'hi', 'octopus']
    """
    for i in range(0, len(lst)):
        _insert_key(lst, i, key)


def _insert_key(lst: list, i: int, key: Optional[Callable] = None) -> None:
    """Move lst[i] so that lst[:i + 1] is sorted.

    If key is not None, sort items based on their return value when passed to key.

    Preconditions:
        - 0 <= i < len(lst)
        - is_sorted(lst[:i])

    >>> lst = ['octopus', 'cat', 'david', 'hi']
    >>> _insert_key(lst, 1)
    >>> lst
    ['cat', 'octopus', 'david', 'hi']
    """
    j = i
    if key is None:
        while not (j == 0 or lst[j - 1] <= lst[j]):
            # Swap lst[j - 1] and lst[j]
            lst[j - 1], lst[j] = lst[j], lst[j - 1]

            j -= 1
    else:
        while not (j == 0 or key(lst[j - 1]) <= key(lst[j])):
            # Swap lst[j - 1] and lst[j]
            lst[j - 1], lst[j] = lst[j], lst[j - 1]

            j -= 1


############################################################################
# Tutorial exercises (grayscale version)
############################################################################
TIME_PER_FRAME = 5  # Number of milliseconds per frame in the animation


def draw_list(screen: pygame.Surface, lst: list[int], row: int) -> None:
    """Render lst as a grid row in the given pygame screen.

    The row parameter specifies the row number to draw the the list in.
    For example, if row = 0, the list is drawn at the top of the screen,
    and if row = len(lst) - 1, the list is drawn at the bottom of the screen.

    Remember that the screen should be divided into an n-by-n grid, where n = len(lst).
    Call screen.get_width, screen.get_height, and/or screen.get_size to determine the
    size of the screen, so that you can calculate the grid cell dimensions.

    Each integer is converted to a greyscale colour for the visualization.

    Preconditions:
        - all(0 <= n <= 255 for n in lst)
        - lst != []
        - 0 <= row < len(lst)
    """
    ...  # Fill this in

    # Update pygame display (don't change this, and keep it at the end of the function body)
    pygame.display.flip()


def visualize_selection_sort(lst: list[int], screen_size: tuple[int, int]) -> None:
    """Visualize selection sort on the given list of integers using pygame.

    Preconditions:
        - all(0 <= n <= 255 for n in lst)
        - lst != []
        - screen_size[0] >= len(lst) and screen_size[1] >= len(lst)

    Implementation notes:
        - We've called initialize_screen to obtain a pygame screen for you
          (you just need to pass it to draw_list).
        - Remember that your code should look very similar to selection sort,
          except with additional calls to draw_list.
        - Call pygame.time.wait to animate the algorithm (drawing one row at a time);
          we've provided a constant that you can use, but feel free to experiment with
          other values as well.
          See https://www.pygame.org/docs/ref/time.html for details.

          NOTE: You won't be able to close the pygame window while the animation is in
          progress, only after it's done. But you can still stop the Python interpreter
          altogether by clicking the red square button in PyCharm.
    """
    screen = initialize_screen(screen_size)

    for i in range(0, len(lst)):
        # NOTE: This is just a sample call to test your draw_list function.
        # You'll need to change this when implementing this function.
        draw_list(screen, lst, 0)

    # Don't remove this! (See function docstring for details)
    wait_for_quit()


def visualize_insertion_sort(lst: list[int], screen_size: tuple[int, int]) -> None:
    """Visualize insertion sort on the given list of integers using pygame.

    Preconditions:
        - all(0 <= n <= 255 for n in lst)
        - lst != []
        - screen_size[0] >= len(lst) and screen_size[1] >= len(lst)
    """
    screen = initialize_screen(screen_size)

    ...

    # Don't remove this! (See function docstring for details)
    wait_for_quit()


################################################################################
# Tutorial exercises (colour version)
################################################################################
def draw_list_colour(screen: pygame.Surface, lst: list[tuple[int, int, int]], row: int) -> None:
    """Render lst as a row in the given pygame screen.

    Similar to draw_list, except now lst is a list of colour RGB tuples.

    Preconditions:
        - all(0 <= n <= 255 for colour in lst for n in colour)
        - lst != []
        - 0 <= row < len(lst)
    """
    cell_width = screen.get_width() / len(lst)
    cell_height = screen.get_height() / len(lst)

    y = int(row * cell_height)

    for i in range(len(lst)):
        colour = lst[i]
        x = int(cell_width * i)
        pygame.draw.rect(screen, colour, (x, y, int(cell_width), int(cell_height)))

    # Update pygame display
    pygame.display.flip()


def visualize_selection_sort_colour(lst: list[tuple[int, int, int]],
                                    screen_size: tuple[int, int]) -> None:
    """Visualize selection sort on the given list of RGB colours using pygame.

    Analogous to visualize_selection_sort.

    Preconditions:
        - all(0 <= n <= 255 for colour in lst for n in colour)
        - lst != []
        - screen_size[0] >= len(lst) and screen_size[1] >= len(lst)
    """
    screen = initialize_screen(screen_size)

    for i in range(len(lst)):
        index_of_smallest = _min_index_key(lst, i, key=rgb_to_hsv)
        lst[index_of_smallest], lst[i] = lst[i], lst[index_of_smallest]

        pygame.time.wait(TIME_PER_FRAME)
        draw_list_colour(screen, lst, i)

    wait_for_quit()


def visualize_insertion_sort_colour(lst: list[tuple[int, int, int]],
                                    screen_size: tuple[int, int]) -> None:
    """Visualize insertion sort on the given list of RGB colours using pygame.

    Analogous to visualize_insertion_sort.

    Preconditions:
        - all(0 <= n <= 255 for colour in lst for n in colour)
        - lst != []
        - screen_size[0] >= len(lst) and screen_size[1] >= len(lst)
    """
    screen = initialize_screen(screen_size)

    for i in range(len(lst)):
        pygame.time.wait(TIME_PER_FRAME)
        draw_list_colour(screen, lst, i)

        _insert_key(lst, o, key=rgb_to_hsv)

    wait_for_quit()


def rgb_to_hsv(colour: tuple[int, int, int]) -> tuple[float, float, float]:
    """Convert an RGB colour representation into the equivalent HSV colour representation.

    For more reading about HSV colour representation, check out
    https://en.wikipedia.org/wiki/HSL_and_HSV.

    Preconditions:
        - all(0 <= c <= 255 for c in colour)

    Note: this function is provided for you, and you shouldn't change it.
    Your responsibility is just to correctly pass this function as the sorting key
    in the appropriate location.
    """
    r, g, b = colour[0] / 255, colour[1] / 255, colour[2] / 255
    x_max = max(r, g, b)
    x_min = min(r, g, b)
    chroma = x_max - x_min
    if x_max == 0:
        saturation = 0
    else:
        saturation = chroma / x_max

    if chroma == 0:
        hue = 0
    elif x_max == r:
        hue = 60 * (g - b) / chroma
    elif x_max == g:
        hue = 60 * (b - r) / chroma + 120
    else:  # x_max == b
        hue = 60 * (r - g) / chroma + 240

    return (hue, saturation, x_max)


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

    import random

    # Sorting, grayscale
    # lst = [random.randint(0, 255) for _ in range(20)]
    # visualize_selection_sort(lst, (400, 400))
    # visualize_insertion_sort(lst, (400, 400))

    # Sorting, colours
    lst = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
           for _ in range(200)]
    visualize_selection_sort_colour(lst, (800, 800))
    visualize_insertion_sort_colour(lst, (800, 800))