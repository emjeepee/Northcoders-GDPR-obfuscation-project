import pytest

from obf_lib.process_csv import process_csv


@pytest.fixture(scope="function")
def general_setup():
    
    pii_fields = ["name", "email"]

    yield_list = [pii_fields]

    yield yield_list



def test_returns_byte_stream(general_setup):
    # Arrange and act:
    



    # Assert:    
    pass