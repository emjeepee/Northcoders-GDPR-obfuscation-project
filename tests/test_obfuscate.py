import pytest
from unittest.mock import Mock, patch

from obf_lib.main          import obfuscate




@pytest.fixture(scope="function")
def general_setup():
    path = "s3://my_ingestion_bucket/new_data/file1.csv"
    bucket = 'my_ingestion_bucket'
    key = 'new_data/file1.csv'
    pii_fields = ['name', 'email']
    input_dict = {'file_to_obfuscate': path, 'pii_fields': pii_fields}
    input_json = """{"file_to_obfuscate": "s3://my_ingestion_bucket/new_data/file1.csv", 'pii_fields': ['name', 'email']}"""

    yield path, bucket, key, pii_fields, input_dict, input_json





def test_calls_internal_functions_correctly_when_input_is_dict(general_setup):
    path, bucket, key, pii_fields, input_dict, input_json = general_setup

    mock_deal_with_csv = Mock(return_value="mocked_byte_stream")
    with patch('obf_lib.main.find_input_type') as mock_fit, \
         patch('obf_lib.main.return_data_type') as mock_rdt, \
         patch('obf_lib.main.get_key_and_bucket_name') as mock_gkabn, \
         patch("obf_lib.main.func_lookup", {"csv": mock_deal_with_csv}):

        mock_fit.return_value = input_dict
        mock_rdt.return_value = 'csv'
        mock_gkabn.return_value = [bucket, key]
        return_val = obfuscate(input_dict)

        mock_fit.assert_called_once_with(input_dict)
        mock_rdt.assert_called_once_with(path)
        mock_gkabn.assert_called_once_with(path)
        mock_deal_with_csv.assert_called_once_with(bucket, key, pii_fields)
        assert return_val == "mocked_byte_stream"



def test_calls_internal_functions_correctly_when_input_is_json_string(general_setup):
    path, bucket, key, pii_fields, input_dict, input_json = general_setup

    mock_deal_with_csv = Mock(return_value="mocked_byte_stream")
    with patch('obf_lib.main.find_input_type') as mock_fit, \
         patch('obf_lib.main.return_data_type') as mock_rdt, \
         patch('obf_lib.main.get_key_and_bucket_name') as mock_gkabn, \
         patch("obf_lib.main.func_lookup", {"csv": mock_deal_with_csv}):

        mock_fit.return_value = input_dict
        mock_rdt.return_value = 'csv'
        mock_gkabn.return_value = [bucket, key]
        return_val = obfuscate(input_json)

        mock_fit.assert_called_once_with(input_json)
        mock_rdt.assert_called_once_with(path)
        mock_gkabn.assert_called_once_with(path)
        mock_deal_with_csv.assert_called_once_with(bucket, key, pii_fields)
        assert return_val == "mocked_byte_stream"
