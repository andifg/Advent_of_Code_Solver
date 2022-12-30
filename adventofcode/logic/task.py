"""Class to manage a single Task of Advent of Code"""

import logging

from adventofcode.logic.inputloader import InputLoader
from adventofcode.logic.solver.solver import Solver
from adventofcode.logic.transformer.inputtransformer import InputTransformer


class Task:
    """Class to manage a single Task of Advent of Code"""

    # pylint: disable=too-few-public-methods

    def __init__(self, inputfile, transformer, solver):
        self.input = InputLoader(inputfile)
        self.transformer = InputTransformer(transformer())
        self.solver = Solver(solver())

    def start(self):
        """Main function for loading, transforming and solving tasks."""
        raw_input = self.input.load_textfile_as_list()
        logging.info("Loaded input")
        logging.debug("Loaded input: %d", raw_input)
        transformed_input = self.transformer.do_transformation(raw_input)
        logging.info("Input transformed")
        logging.debug("Transformed input to: %d", transformed_input)
        result = self.solver.solve(transformed_input)
        logging.info("Solution: %d", result)
