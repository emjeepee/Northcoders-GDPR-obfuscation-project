from obf_lib.return_data_type        import return_data_type
from obf_lib.get_key_and_bucket_name import get_key_and_bucket_name





def obfuscate(input_dict: dict):
    """
    This function:
        reads a file from S3 that is either 
        a .csv file, a .json file or a .parquet 
        file, obfuscates specified PII fields, 
        and returns the modified file as a byte 
        stream.
    
    Args:
        input_dict: a dictionary that has these two 
            keys:
              'file_to_obfuscate'. The value of this 
                key is a string that represents the file 
                path to the file that contains the data 
                among which is the data to obfuscate.
              pii_fields: The value of this key is a 
                list of strings, each string being 
                the name of the field that must be 
                obfuscated. 
    Returns:
        A bytestream that represents a file that 
        is similar to the file specified at the 
        file path but in which the given fields are 
        obfuscated.
    """

    # Get the file path string:
    file_path = input_dict['file_to_obfuscate']

    # get the data type of the file
    # as a string (eg 'json'):
    data_type = return_data_type(file_path)
    
    bucket_key_list = get_key_and_bucket_name(file_path)
    bucket_name = bucket_key_list[0]
    key = bucket_key_list[1]


    # Get the file from the 
    # S3 bucket:
    if data_type == 'csv':
        key

    if data_type == 'json':
        key


    if data_type == 'parquet':
        key
