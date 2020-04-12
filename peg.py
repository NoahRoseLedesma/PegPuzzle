"""
Enum representing the types of pegs in the puzzle.
Each enum value should be the character used to represent this peg in the output
"""
from enum import Enum


class Peg(Enum):
    RED = "R"
    BLUE = "B"
    NONE = "_"
