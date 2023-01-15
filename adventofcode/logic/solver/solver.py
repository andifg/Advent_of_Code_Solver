"""Module to manage execution of solver strategies """

import logging
from typing import Any, List

from adventofcode.logic.solver.solverstrategy import SolverSettings, SolverStrategy


class Solver:
    """Manager class to execute solver strategies"""

    def __init__(self, strategy: list[SolverStrategy]) -> None:
        self.strategy = strategy

    def solve(self, input_data: List) -> List:
        """Execute all strategies from strategies list

        Args:
            input_list (List): List of strategies to execute

        Returns:
            result: result of solver strategies
        """
        if self.strategy:
            logging.debug("Executing solver %d", self.strategy[0])
            solver_setting = self.prepare_input_for_solver_strategies(input_data)
            solver_result = self.strategy[0].solve(solver_setting)
            self.strategy.pop(0)
            return self.solve(solver_result)

        return input_data

    def prepare_input_for_solver_strategies(self, input_data: Any) -> SolverSettings:
        """Create Solver Settings based on Input Data

        Args:
            input_data (Any): Input Data

        Returns:
            SolverSettings: Object with correct attributes
        """
        if any(isinstance(entry, list) for entry in input_data):
            return SolverSettings(input_lists=input_data)
        return SolverSettings(input_list=input_data)
