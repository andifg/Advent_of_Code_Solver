import pytest
from adventofcode.logic.task.task import Task
import unittest.mock as mock

@pytest.fixture
def task():
    solver_strategies = [mock.Mock(return_value="Solverstrategy Mock") for _ in range(3)]
    transformer_strategies = [mock.Mock(return_value="Transformerstrategy Mock") for _ in range(3)]

    obj = Task("Input Mock", transformer_strategies, solver_strategies)

    return obj
