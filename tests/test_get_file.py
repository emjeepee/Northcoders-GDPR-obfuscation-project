import pytest
from obf_lib.get_file import get_file





def test_returns_correct_file():
    # Arrange:
    bucket = 'my_ingestion_bucket'
    key = 'new_data/file1.csv'


    # Act:
    response = get_file(bucket, key)


    # Assert:
    assert False        

    
