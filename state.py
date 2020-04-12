"""
Python class to represent a single "state" in the peg puzzle
Also contains the logic for discovering states
"""
from itertools import chain
from typing import Final, List, Iterable, Generator, Tuple, Callable
from peg import Peg
Operator = Callable[["PuzzleState"], Generator["PuzzleState", None, None]]


class PuzzleState:
    def __init__(self, state: Tuple[Peg], path: List["PuzzleState"]):
        self.__state: Tuple[Peg] = state
        self.__path = path

    # Defines the string representation of a PuzzleState
    def __str__(self) -> str:
        return "".join((peg.value for peg in self.__state))

    def __repr__(self) -> str:
        return str(self)

    # Defines the equality operator on PuzzleState
    def __eq__(self, other: "PuzzleState"):
        return self.state_tuple == other.state_tuple

    @property
    def path(self) -> List["PuzzleState"]:
        return self.__path

    @property
    def state_tuple(self) -> Tuple[Peg]:
        return self.__state

    def get_next_states(self, operators: Iterable[Operator]) -> Generator["PuzzleState", None, None]:
        """
        Apply operators to produce a set of possible next states
        :param operators: A list of callable objects that map a puzzle state to a next possible puzzle state
        :return: The list of possible next states from this state
        """

        # This line is pretty scary so I will break it down
        # Each operator produces a generator of next states.
        # chain.from_iterable consolidates these generators such that they act as a single iterable object
        # then, as states are selected from the chain, those that are None, in the path, and are us get filtered out
        state_chain = chain.from_iterable([operator(self) for operator in operators])
        for state in state_chain:
            if state is not None and state not in self.__path and state != self:
                yield state

    @classmethod
    def from_string(cls, string: str) -> "PuzzleState":
        return PuzzleState(tuple([Peg(char) for char in string]), [])
