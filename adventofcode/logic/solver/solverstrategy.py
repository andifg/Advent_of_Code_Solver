"""Module to manage different solver strategies."""
from abc import ABC, abstractmethod
from typing import List


class SolverStrategy(ABC):
    """
    Abstact class for solver algorithms.

    The Solver Class calls the solver algorithms of the implemented solver classes
    """

    # pylint: disable=too-few-public-methods

    @abstractmethod
    def solve(self, input_list: List):
        """Abstract method to be overrriden."""


class CalculateHighestGroupinList(SolverStrategy):
    """Calculate the highest group in input list."""

    # pylint: disable=too-few-public-methods

    def solve(self, input_list: List[int | str]) -> int:
        """Returns the highest sum of consecutive numbers divided by "" in an
        input list.

        Args:
            data (List): list of numbers or empty entries ("")

        Returns:
            highest_number: Highest group in list seperated by ""
        """
        highest_number = 0
        current_number = 0
        for entry in input_list:
            if entry == "":
                if current_number > highest_number:
                    highest_number = current_number
                current_number = 0
            else:
                current_number += int(entry)
        return highest_number
