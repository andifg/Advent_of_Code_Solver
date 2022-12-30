"""Module to manage execution of solver strategies """

from typing import List

from adventofcode.logic.solver.solverstrategy import SolverStrategy


class Solver:
    """Manager class to execute solver strategies"""

    # pylint: disable=too-few-public-methods

    def __init__(self, strategy: SolverStrategy) -> None:
        self.strategy = strategy

    def solve(self, input_data: List) -> List:
        """_summary_

        Args:
            input_list (List): input list

        Returns:
            result: result of solver strategy
        """

        result = self.strategy.solve(input_data)
        return result
