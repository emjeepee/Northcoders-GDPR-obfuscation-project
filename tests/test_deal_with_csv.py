import pytest
from unittest.mock import Mock, patch

from obf_lib.deal_with_csv import deal_with_csv



@pytest.fixture(scope="function")
def general_setup():
    "s3://my_ingestion_bucket/new_data/file1.csv"
    bucket = 'my_ingestion_bucket'
    key = 'new_data/file1.csv'
    pii_fields = ['name', 'email']


    yield bucket, key, pii_fields



# @pytest.mark.skip
def test_internal_files_called_correctly(general_setup):
    bucket, key, pii_fields = general_setup
    with patch('obf_lib.deal_with_csv.get_file') as mock_gf, \
         patch('obf_lib.deal_with_csv.make_csv_reader_and_writer') as mock_mcraw, \
         patch('obf_lib.deal_with_csv.process_csv') as mock_pc  :
        
        mock_gf.return_value = 'mock_gf_return'
        mock_mcraw.return_value = 'mock_mcraw_return'
        
        deal_with_csv(bucket, key, pii_fields)
        
        mock_gf.assert_called_once_with(bucket, key)
        mock_mcraw.assert_called_once_with('mock_gf_return')
        mock_pc.assert_called_once_with('mock_mcraw_return', pii_fields)
        
        