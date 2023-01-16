from adventofcode.logic.transformer.transfomerstrategy import RemoveNewLinesInListEntries, DivideListToListofLists, RefacterListtoListofListsbySeparator
import pytest


def test_remove_new_lines_in_list_entries():
    # Create an instance of the class that the do_transformation method belongs to
    obj = RemoveNewLinesInListEntries()

    # Test case 1: Ensure that newline characters are removed from the input list
    data = ["Hello\n", "world\n"]
    expected_output = ["Hello", "world"]
    assert obj.do_transformation(data) == expected_output

    # Test case 2: Ensure that no newline characters are removed from the input list
    data = ["Hello", "world"]
    expected_output = ["Hello", "world"]
    assert obj.do_transformation(data) == expected_output

    # Test case 3: Ensure that only newline characters are removed from the input list
    data = ["\n", "\n"]
    expected_output = ["", ""]
    assert obj.do_transformation(data) == expected_output

    # Test case 4: Ensure that empty input list returns an empty list
    data = []
    expected_output = []
    assert obj.do_transformation(data) == expected_output



def test_refactor_list_to_list_of_lists_by_seperator():

    obj = RefacterListtoListofListsbySeparator()

    data = ["1", "2", 3, "", 4]
    expected_output = [[1,2,3], [4]]
    assert obj.do_transformation(data) == expected_output

    data = [2, 1, 3, "", 4 , 3 , 2]
    expected_output = [[2,1,3], [4,3,2]]
    assert obj.do_transformation(data) == expected_output

    data = []
    expected_output = []
    assert obj.do_transformation(data) == expected_output

    data = ["1", "2", "3", "4"]
    expected_output = [[1, 2, 3, 4]]
    assert obj.do_transformation(data) == expected_output


def test_divie_list_into_list_of_lists():
    # Create an instance of the class that the do_transformation method belongs to
    obj = DivideListToListofLists()

    # Test case 1: Ensure that the function splits the elements of the input list by space
    data = ["Hello world", "I am a sentence"]
    expected_output = [["Hello", "world"], ["I", "am", "a", "sentence"]]
    assert obj.do_transformation(data) == expected_output

    # Test case 2: Ensure that the function returns the same input list when the elements of the input list are already splitted
    data = ["Hello", "world"]
    expected_output = [["Hello"], ["world"]]
    assert obj.do_transformation(data) == expected_output

    # Test case 3: Ensure that the function returns an empty list when passed empty input list
    data = []
    expected_output = []
    assert obj.do_transformation(data) == expected_output

    # Test case 4: Ensure that the function returns a list of lists even if the input list contains only one element
    data = ["Hello world"]
    expected_output = [["Hello", "world"]]
    assert obj.do_transformation(data) == expected_output