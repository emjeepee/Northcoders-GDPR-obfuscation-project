


def process_csv(r_w_os_list, pii_fields):
    """
    This function:
        looks in the passed-in csv reader
          for the given PII fields and 
          obfuscates the data under them.
    
    Arguments:
        r_w_os_list: a list that has three 
         members: 
         1) a reader csv object, 
         2) a writer csv object and  
         3) an io.StringIO() output stream 
         that contains only the headers of 
         the .csv file.
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

    for row_dict in r_w_os_list[0]:
        for field in pii_fields:
            row_dict[field] = "***"
        r_w_os_list[1].writerow(row_dict)

    # Convert to byte stream
    byte_stream = r_w_os_list[2].getvalue().encode("utf-8")
    return byte_stream