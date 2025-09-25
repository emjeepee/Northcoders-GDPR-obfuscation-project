import pytest
from obf_lib.get_key_and_bucket_name import get_key_and_bucket_name






def test_returns_list_containing_two_strings():
    # Arrange:
    file_path = 's3://my_ingestion_bucket/new_data/file1.csv'
    expected_0 = list
    expected_1 = str
    expected_2 = str
    expected_3 = 2

    # Act:
    response = get_key_and_bucket_name(file_path)
    result_0 = type(response)
    result_1 = type(response[0])
    result_2 = type(response[1])
    result_3 = len(response)

    # Assert
    assert result_0 == expected_0
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3



# @pytest.mark.skip
def test_returns_correct_strings():
    # Arrange:
    file_path = 's3://my_ingestion_bucket/new_data/file1.csv'
    expected_0 = 'my_ingestion_bucket'
    expected_1 = 'new_data/file1.csv'
    

    # Act:
    response = get_key_and_bucket_name(file_path)
    result_0 = response[0]
    result_1 = response[1]

    # Assert
    # assert result_0 == 'xxx' 
    # assert result_1 == 'yyy'

    assert expected_0 == result_0 
    assert expected_1 == result_1
