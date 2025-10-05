from obf_lib.return_data_type           import return_data_type
from obf_lib.get_key_and_bucket_name    import get_key_and_bucket_name
from obf_lib.deal_with_csv              import deal_with_csv
from obf_lib.deal_with_json             import deal_with_json
from obf_lib.deal_with_parquet          import deal_with_parquet
from obf_lib.func_lookup                import func_lookup




def obfuscate(input_dict: dict):
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
              2) pii_fields: the value of this key 
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

    # Get the file path string:
    file_path = input_dict['file_to_obfuscate']

    # Get the names of the PII fields:
    pii_fields = input_dict['pii_fields']

    # get the data type of the file
    # as a string (eg 'csv', 'json' or 'parquet'):
    data_type = return_data_type(file_path)
    
    # get the bucket name and key name:
    bucket_and_key = get_key_and_bucket_name(file_path)
    bucket = bucket_and_key[0]
    key = bucket_and_key[1]

    # make bytestream:
    obf_byt_strm = func_lookup[data_type](bucket, key, pii_fields)
    
    # return bytestream:
    return obf_byt_strm