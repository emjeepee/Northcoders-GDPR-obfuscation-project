import pytest
import csv

from obf_lib.make_csv_reader_and_writer import make_csv_reader_and_writer



@pytest.fixture(scope="function")
def general_setup():
    mock_csv_content = "id,name,email\n1,Deckard,deckard@test.com\n2,Rachael,rachael@test.com\n3,Roy,roy@test.com"
    response_list = make_csv_reader_and_writer(mock_csv_content)   
    mock_headers = "id,name,email"
    
    # Define a class that the test to ensure 
    # the function under test returns the correct 
    # stringIO object will employ to ensure the
    # test fails:
    class Fail_stringIO:
        def __init__(self):
            self.read = 'fail'
        def seek(self, *args):
            return None

    # Instantiate the object
    fake_strIO = Fail_stringIO() 

    yield_list = [response_list, fake_strIO, mock_headers]
    yield yield_list




def test_returns_a_list(general_setup):
    # Arrange:
    response_list, fake_strIO, mock_headers = general_setup
    # expected = str # to ensure test can fail
    expected = list

    # Act:
    result = type(response_list)

    # Assert:
    assert result == expected




def test_reader_is_DictReader(general_setup):
    # Arrange & act:
    response_list, fake_strIO, mock_headers = general_setup
    # reader = '' # to ensure test can fail
    assert isinstance(response_list[0], csv.DictReader)
    assert response_list[0].fieldnames == ["id", "name", "email"]




def test_writer_is_DictWriter(general_setup):
    # Arrange & act:
    response_list, fake_strIO, mock_headers = general_setup
    # writer = '' # to ensure test can fail
    assert isinstance(response_list[1], csv.DictWriter)
    assert response_list[1].fieldnames == ["id", "name", "email"]




def test_returns_correct_stringIO_object(general_setup):
    # Arrange & act:
    response_list, fake_strIO, mock_headers = general_setup
    # response_list = ['fail', 'fail', 'fail'] # to ensure test can fail at assert isinstance(response_list[2], io.StringIO) 
    # response_list[2] = fake_strIO # to ensure test can fail at assert response_list[2].read == ''
    response_list[2].seek(0)
    # assert isinstance(response_list[2], io.StringIO)
    assert response_list[2].read().strip() == mock_headers

        