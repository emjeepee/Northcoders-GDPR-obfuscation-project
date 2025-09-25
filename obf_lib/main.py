from obf_lib.return_data_type import return_data_type






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

    # get the data type of the file
    # as a string (eg 'json'):
    data_type = return_data_type(input_dict['file_to_obfuscate'])
    
    