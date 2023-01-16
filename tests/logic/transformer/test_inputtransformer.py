import unittest.mock as mock
from adventofcode.logic.transformer.inputtransformer import InputTransformer



def test_input_transformer_do_transformations():

    # Create mocks for the do_transformation method for each transformer
    mock_transformer1 = mock.Mock()
    mock_transformer1.do_transformation.return_value = "transformed by transformer1"
    mock_transformer2 = mock.Mock()
    mock_transformer2.do_transformation.return_value = "transformed by transformer2"
    mock_transformer3 = mock.Mock()
    mock_transformer3.do_transformation.return_value = "transformed by transformer3"

    # set the mocks to the strategy list
    strategies = [mock_transformer1, mock_transformer2, mock_transformer3]

    # Create an instance of the class that the do_transformation method belongs to
    obj = InputTransformer(strategies)

    # Test case 1: Ensure that the function correctly applies all transformations in the correct order
    raw_input = "raw input"
    expected_output = "transformed by transformer3"
    assert obj.do_transformations(raw_input) == expected_output

    # check that the do_transformation method for each transformer is called only once
    mock_transformer1.do_transformation.assert_called_once()
    mock_transformer2.do_transformation.assert_called_once()
    mock_transformer3.do_transformation.assert_called_once()