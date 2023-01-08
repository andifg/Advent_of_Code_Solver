from adventofcode.logic.solver.solverstrategy import CalculateHighestGroupinList, CalculateHighestGroupinListofLists
import pytest


def test_calculate_highest_group_in_List():

    test_object = CalculateHighestGroupinList()

    # Only one group
    assert test_object.solve([5]) == 5
    # Single two groups case
    assert test_object.solve([1, 2]) == 3
    # Three groups case
    assert test_object.solve([1, "", 3, "", 4]) == 4
    # Four groups case
    assert test_object.solve(["", 1, 3, 4, "", 2, ""]) == 8
    # Only ""
    assert test_object.solve(["", "", ""]) == 0


def test_calculate_highest_group_in_List_of_Lists():

    test_object = CalculateHighestGroupinListofLists()

    # Test empty input
    assert test_object.solve([]) == 0

    # Test input with a single list
    assert test_object.solve([[1, 2, 3]]) == 6

    # Test input with multiple lists
    assert test_object.solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 24
    assert test_object.solve([[1, 2, 3], [4, 5, 6], [10, 20, 30]]) == 60

    # Test input with negative numbers
    assert test_object.solve([[-1, -2, -3], [-4, -5, -6], [10, 20, 30]]) == 60
    assert test_object.solve([[-1, -2, -3], [-4, -5, -6], [-10, -20, -30]]) == -6

    # Test input with all zeros
    assert test_object.solve([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
