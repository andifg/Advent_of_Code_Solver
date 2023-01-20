import logging
from adventofcode.logic.task.taskmanager import TaskManager
import pytest
from unittest.mock import Mock, patch


REGISTERED_TASKS_TESTS = {
    "ONE": {
        "input": "01-1.txt",
        "transformers": ["Transformerstrategie1", "Transformerstrategie2"],
        "solver": ["Solverstrategy1"],
    },
    "TWO": {
        "input": "01-1.txt",
        "transformers": ["Transformerstrategie1", "Transformerstrategie2"],
        "solver": ["Solverstrategy1"],
    },
    "THREE": {
        "input": "02-1.txt",
        "transformers": ["Transformerstrategie1", "Transformerstrategie2"],
        "solver": ["Solverstrategy1"],
    },
}


@patch('adventofcode.logic.task.taskmanager.REGISTERED_TASKS', new=REGISTERED_TASKS_TESTS)
@patch('adventofcode.logic.task.taskmanager.Task', new_callable=Mock)
def test_task_manager_solve_single_task(patch_task)-> None:

    obj = TaskManager()

    obj.solve_single_task("THREE")

    patch_task.return_value = "true"

    patch_task.assert_called_once_with("02-1.txt", ['Transformerstrategie1', 'Transformerstrategie2'], ['Solverstrategy1'])


@patch('adventofcode.logic.task.taskmanager.REGISTERED_TASKS', new=REGISTERED_TASKS_TESTS)
def test_solve_all_task(caplog):

    caplog.set_level(logging.DEBUG)


    obj = TaskManager()

    obj.solve_single_task = Mock(return_value="Task solved")

    obj.solve_all_task()

    print(caplog.records)

    assert "######## SOLVING ONE ##########" in caplog.text
    assert "######## SOLVING TWO ##########" in caplog.text
    assert "######## SOLVING THREE ##########" in caplog.text

    assert obj.solve_single_task.call_count == 3
