import pytest

from obf_lib.find_input_type import find_input_type



def test_returns_dict_when_input_is_json():
    # Arrange:
    expected = dict
    inpt = """{"path": "some/path/to/a/file.csv", "pii_fields": ["email", "name"] }"""

    # Act:
    response = find_input_type(inpt)
    result = type(response)

    # Assert:
    # assert expected == 'result' # to ensure test can fail
    assert expected == result



def test_returns_dict_when_input_is_dict():
    # Arrange:
    expected = dict
    inpt = {"path": "some/path/to/a/file.csv", "pii_fields": ["email", "name"] }

    # Act:
    response = find_input_type(inpt)
    result = type(response)

    # Assert:
    # assert expected == 'result' # to ensure test can fail
    assert expected == result    
    