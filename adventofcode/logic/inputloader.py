"""Module to manage loading of different file types."""

from typing import List


class InputLoader:
    """Class for different loader functions."""

    # pylint: disable=too-few-public-methods

    def __init__(self, path: str):
        self.path = path

    def load_textfile_as_list(self) -> List:
        """Load a textfile and return as list.

        Returns:
            inputList: loaded list
        """
        with open("./adventofcode/input/" + self.path, encoding="utf-8") as file:
            input_list: list = file.readlines()
            return input_list
