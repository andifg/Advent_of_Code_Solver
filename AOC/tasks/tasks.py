from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List

REGISTERED_TASKS = {
    "01-01": {
        "input": "01-1.txt",
        "transformer": "RemoveNewLines",
        "solver": "CalculateHighestGroupinList",
    }
}


class Task:
    def __init__(self, input, transformer, solver):
        self.input = InputLoader(input)
        self.transformer = InputTransformer(eval(f"{transformer}()"))
        self.solver = Solver(eval(f"{solver}()"))

    def start(self):
        raw_input = self.input.load_textfile_as_list()
        logging.info("Loaded input")
        logging.debug(f"Loaded input: {raw_input}")
        transformed_input = self.transformer.do_transformation(raw_input)
        logging.info("Input transformed")
        logging.debug(f"Transformed input to: {transformed_input}")
        result = self.solver.solve(transformed_input)
        logging.info(f"Solution: {result}")


class TaskManager:
    taskList: []

    def solve_single_task(self, taskname):
        task = Task(
            REGISTERED_TASKS.get(taskname).get("input"),
            REGISTERED_TASKS.get(taskname).get("transformer"),
            REGISTERED_TASKS.get(taskname).get("solver"),
        )
        task.start()


class InputLoader:
    def __init__(self, path: str):
        self.path = path

    def load_textfile_as_list(self) -> list:
        with open("./AOC/input/" + self.path) as f:
            inputList: list = f.readlines()
            return inputList


class InputTransformer:
    def __init__(self, strategy: TransformerStrategy) -> None:
        self.strategy = strategy

    def do_transformation(self, raw_input):

        result = self.strategy.do_transformation(raw_input)
        return result


class TransformerStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_transformation(self, data: List):
        pass


class RemoveNewLines(TransformerStrategy):
    def do_transformation(self, input: List):
        transformed_input = [item.replace("\n", "") for item in input]
        logging.debug(transformed_input)
        return transformed_input


class Solver:
    def __init__(self, strategy: SolverStrategy) -> None:
        self.strategy = strategy

    def solve(self, input):

        result = self.strategy.solve(input)
        return result


class SolverStrategy(ABC):
    """
    Abstact class for solver algorithms.

    The Solver Class calls the solver algorithms of the implemented solver classes
    """

    @abstractmethod
    def solve(self):
        pass


class CalculateHighestGroupinList(SolverStrategy):
    def solve(self, data: List):
        highest_number = 0
        current_number = 0
        for entry in data:
            if entry == "":
                if current_number > highest_number:
                    highest_number = current_number
                current_number = 0
            else:
                current_number += int(entry)
        return highest_number
