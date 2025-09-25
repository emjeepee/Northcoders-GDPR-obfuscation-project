def return_data_type(file_path_string):
    """
    This function:
        removes the suffix of a file path 
        that is in the form of a string
        and returns that suffix as a string.
    
    Arguments:
        A string that represents a file path
        to the input file in the S3 bucket

    Returns:
        A string that is the suffix of the 
        file path. This will have the value 
        'csv', 'json' or 'parquet'.
    """
    
    suffix_list = file_path_string.split('.')
    suffix = suffix_list[1]
    return suffix



