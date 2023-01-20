from adventofcode.logic.task.task import Task
from adventofcode.logic.inputloader import InputLoader
import unittest.mock as mock



def test_task_init():
    solvers = [mock.Mock() for _ in range(3)]
    transformers = [mock.Mock() for _ in range(3)]

    obj = Task("test_input", transformers, solvers)

    assert obj.input.path == "test_input"
    assert isinstance(obj.input, InputLoader)


    assert all(obj.call_count == 1 for obj in solvers)
    assert all(obj.call_count == 1 for obj in transformers)


def test_task_solver(task):

    task.input.load_textfile_as_list = mock.Mock()
    task.input.load_textfile_as_list.return_value = "Input loaded"
    task.transformer = mock.Mock()
    task.transformer.do_transformations.return_value = "Transformed"
    task.solver = mock.Mock()
    task.solver.solve.return_value = "Solved"

    task.start()

    task.input.load_textfile_as_list.assert_called_once()
    task.transformer.do_transformations.assert_called_once_with("Input loaded")
    task.solver.solve.assert_called_once_with("Transformed")
