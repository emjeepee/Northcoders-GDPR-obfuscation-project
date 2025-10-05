from obf_lib.get_file import get_file



def deal_with_parquet(bucket, key, pii_fields):
    """
    This function:
        gets from the S3 bucket the json file that 
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

    return 