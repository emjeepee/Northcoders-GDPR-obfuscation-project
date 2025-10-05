



def process_json(file, pii_fields):
    """
    This function:
        obfuscates the data under the given 
        PII fields in the passed-in file.
    
    Arguments:
        file: 
        pii_fields: a list of strings, each
          a PII field from the .csv file. 
          The data under these fields must 
          be obfuscated.

    Returns:
        a byte stream that represents the 
        original .csv file but with 
        obfuscated data under the 
        passed-in PII fields.
    """
    return