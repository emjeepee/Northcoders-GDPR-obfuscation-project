import io
import csv





def process_csv(rw_list, pii_fields):
    """
    This function:
        looks in the passed-in file for 
          the given PII fields and 
          obfuscates data in that file
          if the data live under those
          fields.
    
    Arguments:
        file_content: a string that is the 
          contents of a .csv file that 
          previous code has read from the 
          S3 bucket.
        pii_fields: a list of strings, each
          string being a field in the .csv
          file.

    Returns:
        a byte stream in which this 
          function has obfuscated the data 
          under the given PII fields.
    """

    input_stream = io.StringIO(file_content)
    reader = csv.DictReader(input_stream)

    output_stream = io.StringIO()
    writer = csv.DictWriter(output_stream, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row_dict in reader:
        for field in pii_fields:
            row_dict[field] = "***"
        writer.writerow(row_dict)

    # Convert to byte stream
    return output_stream.getvalue().encode("utf-8")