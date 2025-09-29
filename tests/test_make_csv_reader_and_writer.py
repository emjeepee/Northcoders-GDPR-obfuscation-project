import pytest
import csv

from obf_lib.make_csv_reader_and_writer import make_csv_reader_and_writer


mock_csv_content = """id,name,email\n
1,Deckard,deckard@test.com\n
2,Rachael,rachael@test.com\n
3,Roy,roy@test.com\n
                    """


def test_returns_a_list():
    # Arrange:
    # expected = str # to ensure test can fail
    expected = list

    # Act:
    response = make_csv_reader_and_writer(mock_csv_content)
    result = type(response)

    # Assert:
    assert result == expected



def test_reader_is_DictReader():
    # Arrange & act:
    # reader = '' # to ensure test can fail
    reader, writer = make_csv_reader_and_writer(mock_csv_content)
    assert isinstance(reader, csv.DictReader)
    assert reader.fieldnames == ["id", "name", "email"]


def test_writer_is_DictWriter():
    # Arrange & act:
    # writer = '' # to ensure test can fail
    reader, writer = make_csv_reader_and_writer(mock_csv_content)
    assert isinstance(writer, csv.DictWriter)
    assert writer.fieldnames == ["id", "name", "email"]
    