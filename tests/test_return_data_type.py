import pytest
from src.return_data_type import return_data_type




@pytest.fixture(scope="function")
def file_path_strings():
    csv_file_path = 's3://some_bucket_name/new_data/file1.csv'
    json_file_path = 's3://some_bucket_name/new_data/file1.json'
    parquet_file_path = 's3://some_bucket_name/new_data/file1.parquet'


    yield_list = [csv_file_path, json_file_path, parquet_file_path]

    yield yield_list
    




def test_returns_string(file_path_strings):
    # Arrange:
    expected_all = str
    file_path_csv  = file_path_strings[0]
    file_path_json = file_path_strings[1]
    file_path_pq   = file_path_strings[2]

    # Act:
    suffix_0 = return_data_type(file_path_csv)
    suffix_1 = return_data_type(file_path_json)
    suffix_2 = return_data_type(file_path_pq)

    type_0 = type(suffix_0)
    type_1 = type(suffix_1)
    type_2 = type(suffix_2)
        
    # Assert:
    assert type_0 == expected_all
    assert type_1 == expected_all
    assert type_2 == expected_all


def test_returns_correct_suffix(file_path_strings):
    # Arrange:
    expected_0 = 'csv'
    expected_1 = 'json'
    expected_2 = 'parquet'
    file_path_csv  = file_path_strings[0]
    file_path_json = file_path_strings[1]
    file_path_pq   = file_path_strings[2]

    # Act:
    result_0 = return_data_type(file_path_csv)
    result_1 = return_data_type(file_path_json)
    result_2 = return_data_type(file_path_pq)

        
    # Assert:
    assert result_0 == expected_0
    assert result_1 == expected_1
    assert result_2 == expected_2
