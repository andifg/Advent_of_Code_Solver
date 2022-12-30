""" Module to manager multiple tasks."""
from __future__ import annotations

from typing import List

from adventofcode.logic.solver.solverstrategy import CalculateHighestGroupinList
from adventofcode.logic.task import Task
from adventofcode.logic.transformer.transfomerstrategy import RemoveNewLines

REGISTERED_TASKS = {
    "01-01": {
        "input": "01-1.txt",
        "transformer": RemoveNewLines,
        "solver": CalculateHighestGroupinList,
    }
}


class TaskManager:
    """Class for managing multiple advent of code tasks.

    Attributes:
        taskList: List of all tasks that will be solved

    """

    # pylint: disable=too-few-public-methods

    taskList: List = []

    def solve_single_task(self, taskname: str):
        """_summary_

        Args:
            taskname (str): Name of the task to be solved
        """
        task = Task(
            REGISTERED_TASKS.get(taskname, {}).get("input"),
            REGISTERED_TASKS.get(taskname, {}).get("transformer"),
            REGISTERED_TASKS.get(taskname, {}).get("solver"),
        )
        task.start()
