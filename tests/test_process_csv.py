import pytest
import io
import csv


from obf_lib.process_csv import process_csv


@pytest.fixture(scope="function")
def general_setup():
    csv_data = """name,email,age
                Jean-Luc,jean-luc@email.com,50
                James,james@email.com,45
                Kathryn,kathryn@email.com,35
                """        
    
    input_stream = io.StringIO(csv_data)

    output_stream = io.StringIO()

    reader = csv.DictReader(input_stream)

    writer = csv.DictWriter(output_stream, fieldnames=reader.fieldnames)
    writer.writeheader()

    r_w_os_list = [reader, writer, output_stream]

    pii_fields = ["name", "email"]

    byt_strm = process_csv(r_w_os_list, pii_fields)
    
    output = r_w_os_list[2].getvalue()

    yield_list = [csv_data, pii_fields, r_w_os_list, byt_strm, output]

    yield yield_list


# @pytest.mark.skip
def test_returns_byte_stream(general_setup):
    # Arrange and act:
    csv_data, pii_fields, r_w_os_list, byt_strm, output = general_setup

    # Assert:
    assert isinstance(byt_strm, bytes)



# @pytest.mark.skip
def test_obfuscates_data_but_only_under_pii_fields(general_setup):
    # Arrange and act:
    csv_data, pii_fields, r_w_os_list, byt_strm, output = general_setup

    # Assert:    
    assert 'Jean-Luc' not in output
    assert 'James' not in output
    assert 'Kathryn' not in output
    assert 'jean-luc@email.com' not in output
    assert 'james@email.com' not in output
    assert 'kathryn@email.com' not in output
    assert "***,***,50" in output
    assert "***,***,45" in output
    assert "***,***,35" in output


# @pytest.mark.skip
def test_returns_correct_encoding(general_setup):
    # Arrange and act:
    csv_data, pii_fields, r_w_os_list, byt_strm, output = general_setup

    # Assert:    
    assert byt_strm.decode("utf-8") == output    