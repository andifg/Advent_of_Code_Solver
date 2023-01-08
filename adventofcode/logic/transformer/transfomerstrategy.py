""" Module to manage different transformer strategies."""
import logging
from abc import ABC, abstractmethod
from typing import List


class TransformerStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    # pylint: disable=too-few-public-methods

    @abstractmethod
    def do_transformation(self, data: List) -> List:
        """Abstract transfomration method to be overwritten."""


class RemoveNewLines(TransformerStrategy):
    """Remove new line characters '\n' from list entries"""

    # pylint: disable=too-few-public-methods

    def do_transformation(self, data: List) -> List:
        """Execute replacement

        Args:
            input (List): input list

        Returns:
            transformed_input: list without new line characters
        """
        transformed_input = [item.replace("\n", "") for item in data]
        logging.debug(transformed_input)
        return transformed_input


class RefacterListtoListofListsbySeparator(TransformerStrategy):
    """TransformerStrategy (_type_): _description_"""

    # pylint: disable=too-few-public-methods

    def __init__(self, seperator: str = ""):
        self.seperator = seperator

    def do_transformation(self, data: List) -> List[List[int]]:
        new_list: List[List[int]] = []
        current_list: List[int] = []
        for item in data:
            if item == "":
                new_list.append(current_list)
                current_list = []
            else:
                current_list.append(int(item))
        return new_list
