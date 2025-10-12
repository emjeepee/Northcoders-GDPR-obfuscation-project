from .get_file import get_file
from .make_csv_reader_and_writer import make_csv_reader_and_writer
from .process_csv import process_csv


def deal_with_csv(bucket, key, pii_fields):
    """
    This function:
        gets from the S3 bucket the csv file that
        contains the PII fields, obfuscates
        the data under those fields and returns
        the new version of the file as a byte
        stream.

    Args:
        bucket: a string for the name of the S3
            bucket in which the file is stored.
        key: the key under which the S3 bucket
            stores the file.
        pii_fields: a list of strings, each
            string being the name of a field
            whose data must be obfuscated.

    Returns:
        A byte stream that is similar to the
            file in the S3 bucket but in which
            the data under the given PII fields
            are obfuscated.
    """
    # Get the file from the
    # S3 bucket:
    file_content = get_file(bucket, key)

    # Make list containing csv
    # reader and writer:
    csv_rw_list = make_csv_reader_and_writer(file_content)

    # obfuscate the data under
    # the given PII fields and
    # return the file as a byte
    # stream:
    obf_byt_strm = process_csv(csv_rw_list, pii_fields)

    return obf_byt_strm
