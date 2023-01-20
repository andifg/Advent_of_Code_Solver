""" Module to manager multiple tasks."""
from __future__ import annotations

import logging
from typing import List

from adventofcode.logic.solver.solverstrategy import (
    CalculateHighestGroupinList,
    CalculateHighestGroupinListofLists,
    CalculateSumofTopThreeGroupsinListofLists,
    CalculateRockPaperScissorsStrategyScore
)
from adventofcode.logic.task.task import Task
from adventofcode.logic.transformer.transfomerstrategy import (
    RefacterListtoListofListsbySeparator,
    RemoveNewLinesInListEntries,
    DivideListToListofLists
)

REGISTERED_TASKS = {
    "01-01": {
        "input": "01-1.txt",
        "transformers": [RemoveNewLinesInListEntries, RefacterListtoListofListsbySeparator],
        "solver": [CalculateHighestGroupinList],
    },
    "01-01": {
        "input": "01-1.txt",
        "transformers": [RemoveNewLinesInListEntries, RefacterListtoListofListsbySeparator],
        "solver": [CalculateHighestGroupinListofLists],
    },
    "02-01": {
        "input": "02-1.txt",
        "transformers": [RemoveNewLinesInListEntries, DivideListToListofLists],
        "solver": [CalculateRockPaperScissorsStrategyScore],
    },
}


class TaskManager:
    """Class for managing multiple advent of code tasks.

    Attributes:
        taskList: List of all tasks that will be solved

    """

    # pylint: disable=too-few-public-methods

    taskList: List = []

    def solve_single_task(self, taskname: str) -> None:
        """_summary_

        Args:
            taskname (str): Name of the task to be solved
        """
        task = Task(
            str(REGISTERED_TASKS.get(taskname, {}).get("input", "")),
            list(REGISTERED_TASKS.get(taskname, {}).get("transformers", [])),
            list(REGISTERED_TASKS.get(taskname, {}).get("solver", [])),
        )
        task.start()

    def solve_all_task(self) -> None:
        """Solve all tasks registered."""
        tasks = REGISTERED_TASKS.keys()
        for task in tasks:
            logging.info("######## SOLVING %s ##########", task)
            self.solve_single_task(task)
