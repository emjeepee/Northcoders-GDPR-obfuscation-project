from obf_lib.return_data_type           import return_data_type
from obf_lib.get_key_and_bucket_name    import get_key_and_bucket_name
from obf_lib.find_input_type            import find_input_type
from obf_lib.func_lookup                import func_lookup




def obfuscate(input):
    """
    This function:
        reads a file from an S3 bucket. The file 
        is either 
          i)   a .csv file, 
          ii)  a .json file or 
          iii) a .parquet file.
        This function obfuscates fields that 
        contain personally identifiable 
        information (PII) and returns the 
        modified file as a byte stream.
    
    Args:
        input_dict: a dictionary with these two 
            keys:
              1) 'file_to_obfuscate'. The value of 
                this key is a string that represents 
                the file path to the file that 
                contains the data (and among which 
                is the data to obfuscate).
                The value of this key takes this 
                form: 
                "s3://my_ingestion_bucket/new_data/file1.csv"
              2) 'pii_fields': the value of this key 
                is a list of strings, each string 
                being the name of a field under which 
                peronally identifiable information 
                (PII) is stored that this function 
                must obfuscate. 

    Returns:
        A bytestream that represents a file 
        similar to the file specified at the given
        file path but with obfuscated data in the 
        given PII fields.
    """

    # ensure this function has a 
    # Python dictionary to work on:
    input_dict = find_input_type(input)

    # Get the file path string and :
    # the names of the PII fields:
    file_path, pii_fields = input_dict['file_to_obfuscate'], input_dict['pii_fields']

    # get the data type of the file
    # as a string (eg 'csv', 'json' or 'parquet'):
    data_type = return_data_type(file_path)
    
    # get the bucket name and key name:
    bucket, key = get_key_and_bucket_name(file_path)

    # make bytestream. the following line 
    # employs lookup table func_lookup
    # to call a specific function 
    # depending on the value of 
    # data_type, passing the function 
    # the arguments bucket, key and pii_fields:
    obf_byt_strm = func_lookup[data_type](bucket, key, pii_fields)
    
    # return bytestream:
    return obf_byt_strm