"""Module to manage different solver strategies."""
from abc import ABC, abstractmethod
from typing import List
import logging


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

class CalculateHighestGroupinListofLists(SolverStrategy):
    """Calculate the highest group in input list of lists."""

    # pylint: disable=too-few-public-methods

    def solve(self, input_lists: List[List[int]]) -> int:
        """Returns the highest sum of within a list of lists.

        Args:
            data (List): list of lists with numbers

        Returns:
            highest_number: highest sum of a single list
        """
        logging.info("Solve by calculating highest group in List of Lists")
        return max([sum(list) for list in input_lists])