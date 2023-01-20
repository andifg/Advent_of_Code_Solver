from adventofcode.logic.inputloader import InputLoader
from unittest.mock import mock_open, patch



def test_inputloader_init():

    obj = InputLoader("testpath")


    assert obj.path == "testpath"



@patch("builtins.open", mock_open(read_data="line1\nline2\nline3"))
def test_inputloader_load_textfile_as_list():
    """ Tests whether input is loaded correctly."""
    test_obj = InputLoader("testfile.txt")
    input_list = test_obj.load_textfile_as_list()
    assert input_list == ["line1\n", "line2\n", "line3"]