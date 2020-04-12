"""
An operator is a callable object representing an operation that when applied to a puzzle state, produces a generator of
possible next states.
This file defines the abstract base class for operators and the operators used in the peg puzzle
"""
from typing import Generator, Tuple, Callable
from state import PuzzleState
from peg import Peg
import state


def next_states(start_state: PuzzleState, find: Tuple[Peg, ...], replace: Tuple[Peg, ...])\
        -> Generator[PuzzleState, None, None]:
    """
    Generate states by applying a replacement rule
    :param start_state: The initial state
    :param find: The sequence of pegs to find
    :param replace: The sequence of pegs to replace
    :return: Yields all possible replacement states

    Example: In "R_R_BB" find R_ and replace with _R would produce "_RR_BB" and "R__RBB"
    """
    start_state.path.append(start_state)
    for peg_index in range(len(start_state.state_tuple)):
        if start_state.state_tuple[peg_index:peg_index + len(find)] == find:
            new_state_array = list(start_state.state_tuple)
            new_state_array[peg_index:peg_index + len(find)] = replace
            yield PuzzleState(tuple(new_state_array), start_state.path)
    start_state.path.pop()


def RedSlideOperator(start_state: PuzzleState) -> Generator[PuzzleState, None, None]:
    return next_states(start_state, (Peg.RED, Peg.NONE), (Peg.NONE, Peg.RED))


def BlueSlideOperator(start_state: PuzzleState) -> Generator[PuzzleState, None, None]:
    return next_states(start_state, (Peg.NONE, Peg.BLUE), (Peg.BLUE, Peg.NONE))


def RedJumpOperator(start_state: PuzzleState) -> Generator[PuzzleState, None, None]:
    yield from next_states(start_state, (Peg.RED, Peg.BLUE, Peg.NONE), (Peg.NONE, Peg.BLUE, Peg.RED))
    yield from next_states(start_state, (Peg.RED, Peg.RED, Peg.NONE), (Peg.NONE, Peg.RED, Peg.RED))


def BlueJumpOperator(start_state: PuzzleState) -> Generator[PuzzleState, None, None]:
    yield from next_states(start_state, (Peg.NONE, Peg.RED, Peg.BLUE), (Peg.BLUE, Peg.RED, Peg.NONE))
    yield from next_states(start_state, (Peg.NONE, Peg.BLUE, Peg.BLUE), (Peg.BLUE, Peg.BLUE, Peg.NONE))
