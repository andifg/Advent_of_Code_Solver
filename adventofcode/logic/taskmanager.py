""" Module to manager multiple tasks."""
from __future__ import annotations

from typing import List

from adventofcode.logic.solver.solverstrategy import CalculateHighestGroupinListofLists
from adventofcode.logic.task import Task
from adventofcode.logic.transformer.transfomerstrategy import (
    RefacterListtoListofListsbySeparator,
    RemoveNewLines,
)

REGISTERED_TASKS = {
    "01-01": {
        "input": "01-1.txt",
        "transformers": [RemoveNewLines, RefacterListtoListofListsbySeparator],
        "solver": [CalculateHighestGroupinListofLists],
    }
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
