"""
Peg puzzle game
An example of state-space search
"""
from state import PuzzleState
from operators import RedSlideOperator, RedJumpOperator, BlueSlideOperator, BlueJumpOperator

import sys


def peg_puzzle(start_state_str: str, goal_state_str: str):
    start_state = PuzzleState.from_string(start_state_str)
    goal_state = PuzzleState.from_string(goal_state_str)

    # The order of these operators is the order in which they are applied
    operators = [RedSlideOperator, RedJumpOperator, BlueSlideOperator, BlueJumpOperator]

    def solve(cur_state: PuzzleState):
        if cur_state == goal_state:
            return cur_state.path + [cur_state]
        for next_state in cur_state.get_next_states(operators):
            result = solve(next_state)
            if result is not None:
                return result
        return None

    solution = solve(start_state)
    if solution is None:
        print("There is no solution to this game.")
    else:
        print(solution)


if __name__ == "__main__":
    peg_puzzle(sys.argv[1], sys.argv[2])
