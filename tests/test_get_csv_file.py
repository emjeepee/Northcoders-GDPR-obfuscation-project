import boto3
import pytest
import os

from moto import mock_aws
from obf_lib.get_csv_file import get_csv_file




@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture(scope="function")
def general_setup():
    with mock_aws():
        mock_S3_client = boto3.client("s3", region_name="eu-west-2")
        # 's3://my_ingestion_bucket/new_data/file1.csv'
        bucket_name = 'my_ingestion_bucket'
        key = 'new_data/test_file1.csv'
        mock_S3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
                                    )

        # Upload mock CSV file:
        csv_content = "id,name,email\n1,Keir,keir@test.com\n2,Kemi,kemi@test.com\n3,Mukund,mukund@test.com"
        mock_S3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=csv_content.encode("utf-8")
                                 )    

        yield bucket_name, key




def test_returns_string(general_setup):
    # Arrange:
    (bucket_name, key) = general_setup
    # expected = list # to ensure test can fail
    expected = str

    # Act:
    file_content = get_csv_file(bucket_name, key)
    result = type(file_content)

    # Assert:
    assert result == expected





def test_returns_correct_file(general_setup):
    # Arrange:
    (bucket_name, key) = general_setup

    # Act:
    file_content = get_csv_file(bucket_name, key)

    # Assert:
    # assert file.startswith("id,Name") # when uncommented ensures test is failable
    assert file_content.startswith("id,name,email")
    # assert "1,keith,keir@test.com" in file  # when uncommented ensures test is failable
    assert "1,Keir,keir@test.com" in file_content
    # assert "2,Kevin,kemi@test.com" in file  # when uncommented ensures test is failable
    assert "2,Kemi,kemi@test.com" in file_content
    # assert "3,Mooo,mukund@test.com" in file  # when uncommented ensures test is failable
    assert "3,Mukund,mukund@test.com" in file_content
    
