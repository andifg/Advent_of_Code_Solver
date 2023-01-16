from adventofcode.logic.solver.solver import Solver, SolverSettings
import unittest.mock as mock

def test_solver_solver_execution_without_strategy():
    obj = Solver([])

    input_data = "Input data equals expected data"
    assert input_data == obj.solve(input_data)

def test_solver_solver_execution_with_multiple_strategies():
    mock_strategy1 = mock.Mock()
    mock_strategy1.solve.return_value = "solved by strategy 1"
    mock_strategy2 = mock.Mock()
    mock_strategy2.solve.return_value = "solved by strategy 2"
    mock_strategy3 = mock.Mock()
    mock_strategy3.solve.return_value = "solved by strategy 3"

    strategies = [mock_strategy1, mock_strategy2, mock_strategy3]

    obj = Solver(strategies)

    assert obj.solve("input_data") == "solved by strategy 3"

    mock_strategy1.solve.assert_called_once()
    mock_strategy2.solve.assert_called_once()
    mock_strategy3.solve.assert_called_once()



def test_prepare_input_for_solver_strategies_list():
    input_data = [[1, 2, 3], [4, 5, 6]]
    solver = Solver([])
    result = solver.prepare_input_for_solver_strategies(input_data)
    assert isinstance(result, SolverSettings)
    assert result.input_lists == input_data

def test_prepare_input_for_solver_strategies_non_list():
    input_data = [1, 2, 3, 4]
    solver = Solver([])
    result = solver.prepare_input_for_solver_strategies(input_data)
    assert isinstance(result, SolverSettings)
    assert result.input_list == input_data

def test_prepare_input_for_solver_strategies_string():
    input_data = 'abc'
    solver = Solver([])
    result = solver.prepare_input_for_solver_strategies(input_data)
    assert isinstance(result, SolverSettings)
    assert result.input_list == input_data