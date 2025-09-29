from obf_lib.return_data_type        import return_data_type
from obf_lib.get_key_and_bucket_name import get_key_and_bucket_name
from obf_lib.get_csv_file            import get_csv_file
from obf_lib.process_csv             import process_csv
from obf_lib.process_json            import process_json
from obf_lib.process_parquet         import process_parquet


def obfuscate(input_dict: dict):
    """
    This function:
        reads a file from an S3 bucket. The file 
        is either 
        a .csv file file, 
        a .json file or 
        a .parquet file.
        This function obfuscates fields that 
        contain personally identifiable 
        information (PII) and returns the 
        modified file as a byte stream.
    
    Args:
        input_dict: a dictionary that has these two 
            keys:
              1) 'file_to_obfuscate'. The value of 
                this key is a string that represents 
                the file path to the file that 
                contains the data (and among which 
                is the data to obfuscate.
              2) pii_fields: the value of this key 
                is a list of strings, each string 
                being the name of a field that code 
                will obfuscate. 

    Returns:
        A bytestream that represents a file 
        similar to the file specified at the given
        file path but with obfuscated data in the 
        given fields.
    """

    # make lookup table:
    lookup = {
            "csv": process_csv,
            "json": process_json,
            "parquet": process_parquet
             }



    # Get the file path string:
    file_path = input_dict['file_to_obfuscate']

    # Get the names of the PII fields:
    pii_fields = input_dict['pii_fields']

    # get the data type of the file
    # as a string (eg 'json'):
    data_type = return_data_type(file_path)
    
    bucket_key_list = get_key_and_bucket_name(file_path)
    bucket_name = bucket_key_list[0]
    key = bucket_key_list[1]


    # Get the file from the 
    # S3 bucket:
    file = get_file(bucket_name, key)

    # obfuscate the data under 
    # the given PII fields and
    # return the file as a byte 
    # stream:
    return lookup[data_type](file, pii_fields)

