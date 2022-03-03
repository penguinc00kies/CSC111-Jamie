"""CSC111 Winter 2021 Assignment 2: Trees, Chess, and Artificial Intelligence (Part 2)

Instructions (READ THIS FIRST!)
===============================

This Python module contains the start of functions and/or classes you'll define
for Part 2 of this assignment. Please note that in addition to this file, you will
also need to modify a2_game_tree.py by following the instructions on the assignment
handout. You should NOT make any changes to a2_minichess.py.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu, and Isaac Waller.
"""
import random
from typing import Optional

import a2_game_tree
import a2_minichess


def generate_complete_game_tree(root_move: str, game_state: a2_minichess.MinichessGame,
                                d: int) -> a2_game_tree.GameTree:
    """Generate a complete game tree of depth d for all valid moves from the current game_state.

    For the returned GameTree:
        - Its root move is root_move.
        - Its `is_white_move` attribute is set using the current game_state.
        - It contains all possible move sequences of length <= d from game_state.
          For each node in the tree, its subtrees appear in the same order that their
          moves were returned by game_state.get_valid_moves(),
        - If d == 0, a size-one GameTree is returned.

    Note that some paths down the tree may have length < d, because they result in an end state
    (win or draw) from game_state in fewer than d moves.

    Preconditions:
        - d >= 0
        - root_move == GAME_START_MOVE or root_move is a valid chess move
        - if root_move == GAME_START_MOVE, then game_state is in the initial game state

    Implementation hints:
        - This function must be implemented recursively.
        - In the recursive step, use the MinichessGame.copy_and_make_move method to create
          a copy of the game state with one new move made.
        - You'll need to review the public interface of the MinichessGame class to see what
          methods are available to help implement this function.

    WARNING: we recommend not calling this function with depth greater than 6, as this will
    likely take a very long time on your computer.
    """
    if root_move == '*':
        if d == 0:
            return a2_game_tree.GameTree('*')
        else:
            root = a2_game_tree.GameTree('*')
            for valid_move in a2_minichess.MinichessGame().get_valid_moves():
                new_game_tree = generate_complete_game_tree(valid_move, game_state, d - 1)
                root.add_subtree(new_game_tree)
            return root
    elif d == 0:
        leaf = a2_game_tree.GameTree(root_move, is_white_move=not game_state.is_white_move())
        new_game_state = game_state.copy_and_make_move(root_move)
        if new_game_state.get_winner() == 'White':
            leaf.white_win_probability = 1.0
        else:
            leaf.white_win_probability = 0.0
        return leaf
    else:
        root = a2_game_tree.GameTree(root_move, is_white_move= not game_state.is_white_move())
        new_game_state = game_state.copy_and_make_move(root_move)
        if new_game_state.get_winner() == 'White':
            root.white_win_probability = 1.0
            return root
        elif new_game_state.get_winner() == 'Black' or new_game_state.get_winner() == 'Draw':
            root.white_win_probability = 0.0
            return root

        for valid_move in new_game_state.get_valid_moves():
            new_game_tree = generate_complete_game_tree(valid_move, new_game_state, d-1)
            root.add_subtree(new_game_tree)
        return root


class GreedyTreePlayer(a2_minichess.Player):
    """A Minichess player that plays greedily based on a given GameTree.

    See assignment handout for description of its strategy.
    """
    # Private Instance Attributes:
    #   - _game_tree:
    #       The GameTree that this player uses to make its moves. If None, then this
    #       player just makes random moves.
    _game_tree: Optional[a2_game_tree.GameTree]

    def __init__(self, game_tree: a2_game_tree.GameTree) -> None:
        """Initialize this player.

        Preconditions:
            - game_tree represents a game tree at the initial state (root is '*')
        """
        self._game_tree = game_tree

    def make_move(self, game: a2_minichess.MinichessGame, previous_move: Optional[str]) -> str:
        """Make a move given the current game.

        previous_move is the opponent player's most recent move, or None if no moves
        have been made.

        Preconditions:
            - There is at least one valid move for the given game
        """
        if previous_move is not None:
            for gt in self._game_tree.get_subtrees():
                if gt.move == previous_move:
                    self._game_tree = gt

        if self._game_tree is not None and self._game_tree.get_subtrees() != []:
            subtrees = self._game_tree.get_subtrees()
            if game.is_white_move() == True:
                best_move = subtrees[0]
                for move in subtrees:
                    if move.white_win_probability > best_move.white_win_probability:
                        best_move = move
                self._game_tree = best_move
                return best_move.move
            elif game.is_white_move() == False:
                worst_move = subtrees[0]
                for move in subtrees:
                    if move.white_win_probability < worst_move.white_win_probability:
                        worst_move = move
                self._game_tree = worst_move
                return worst_move.move
        else:
            move = random.choice(game.get_valid_moves())
            return move


def part2_runner(d: int, n: int, white_greedy: bool) -> None:
    """Create a complete game tree with the given depth, and run n games where
    one player is a GreedyTreePlayer and the other is a RandomPlayer.

    The GreedyTreePlayer uses the complete game tree with the given depth.
    If white_greedy is True, the White player is the GreedyTreePlayer and Black is a RandomPlayer.
    This is switched when white_greedy is False.

    Precondtions:
        - d >= 0
        - n >= 1

    Implementation notes:
        - Your implementation MUST correctly call a2_minichess.run_games. You may choose
          the values for the optional arguments passed to the function.
    """
    game = a2_minichess.MinichessGame()
    gt = generate_complete_game_tree('*', game, d)
    if white_greedy:
        white = GreedyTreePlayer(gt)
        black = a2_minichess.RandomPlayer()
    else:
        white = a2_minichess.RandomPlayer()
        black = GreedyTreePlayer(gt)

    a2_minichess.run_games(n, white, black)


# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'max-line-length': 100,
#         'max-nested-blocks': 4,
#         'disable': ['E1136'],
#         'extra-imports': ['random', 'a2_minichess', 'a2_game_tree']
#     })

    # Sample call to part2_runner (you can change this, just keep it in the main block!)
    # part2_runner(5, 50, False)
