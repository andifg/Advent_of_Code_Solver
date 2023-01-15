"""Module to manage a single Task of Advent of Code"""

import json
import logging
from typing import List

from adventofcode.logic.inputloader import InputLoader
from adventofcode.logic.solver.solver import Solver
from adventofcode.logic.transformer.inputtransformer import InputTransformer


class Task:
    """Class to manage a single Task of Advent of Code"""

    # pylint: disable=too-few-public-methods

    def __init__(self, inputfile: str, transformers: List, solvers: List):
        self.input = InputLoader(inputfile)
        self.transformer = InputTransformer(
            [transformer() for transformer in transformers]
        )
        self.solver = Solver([solver() for solver in solvers])

    def start(self) -> None:
        """Main function for loading, transforming and solving tasks."""
        raw_input = self.input.load_textfile_as_list()
        logging.info("Loaded input")
        logging.debug("Loaded input: %d", json.dumps(raw_input))
        transformed_input = self.transformer.do_transformations(raw_input)
        logging.info("Input transformed")
        logging.debug("Transformed input to: %d", transformed_input)
        result = self.solver.solve(transformed_input)
        logging.info("Solution: %d", result)
