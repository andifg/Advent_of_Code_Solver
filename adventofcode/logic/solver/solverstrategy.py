"""Module to manage different solver strategies."""
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class SolverSettings:
    """Class to store settings like input types or seperators for solver strategies"""

    input_list: List[Any] = field(default_factory=list)
    input_lists: List[List[Any]] = field(default_factory=list)


class SolverStrategy(ABC):
    """
    Abstact class for solver algorithms.

    The Solver Class calls the solver algorithms of the implemented solver classes
    """

    # pylint: disable=too-few-public-methods

    @abstractmethod
    def solve(self, settings: SolverSettings) -> Any:
        """Abstract method to be overrriden."""


class CalculateHighestGroupinList(SolverStrategy):
    """Calculate the highest group in input list."""

    # pylint: disable=too-few-public-methods

    def solve(self, settings: SolverSettings) -> int:
        """Returns the highest sum of consecutive numbers divided by "" in an
        input list.

        Args:
            data (List): list of numbers or empty entries ("")

        Returns:
            highest_number: Highest group in list seperated by ""
        """
        highest_number = 0
        current_number = 0

        for entry in settings.input_list:
            if entry != "":
                current_number += int(entry)
            if entry in ("", settings.input_list[len(settings.input_list) - 1]):
                if current_number > highest_number:
                    highest_number = current_number
                current_number = 0

        return highest_number


class CalculateHighestGroupinListofLists(SolverStrategy):
    """Calculate the highest group in input list of lists."""

    # pylint: disable=too-few-public-methods

    def solve(self, settings: SolverSettings) -> int:
        """Returns the highest sum of within a list of lists.

        Args:
            data (List): list of lists with numbers

        Returns:
            highest_number: highest sum of a single list
        """
        logging.info("Solve by calculating highest group in List of Lists")
        try:
            highest_number = max(sum(list) for list in settings.input_lists)
        except ValueError:
            highest_number = 0

        return highest_number


class CalculateSumofTopThreeGroupsinListofLists(SolverStrategy):
    """Return sum of the groups having the largest three sums."""

    # pylint: disable=too-few-public-methods

    def solve(self, settings: SolverSettings) -> int:

        input_lists: List[List[int]] = settings.input_lists

        sorted_lists = sorted(input_lists, key=sum, reverse=True)

        # take the first three elements
        top_three = sorted_lists[:3]

        # calculate the sum of the top three lists
        sum_of_top_three = sum(sum(entry) for entry in top_three)

        return sum_of_top_three

class CalculateRockPaperScissorsStrategyScore(SolverStrategy):
    """Calculate score for RockPaperScissors strategy

    This solver calculates the score for a game strategy. The game strategy
    consists of pairs of choices. Each choice stands for either Rock, Paper or
    Scissor. The first input is always from the enemy the second from the player.
    The score is based on two parts:
    - The player always gets points for his choice (Rock = 1, Paper = 2,
      Scissors = 3)
    - The player gets points for the outcome of the game (Loss = 0, Draw = 3,
      Win = 6)

    """

    # pylint: disable=too-few-public-methods

    def solve(self, settings: SolverSettings) -> int:

        breakpoint()

        return None