import io
import csv





def process_csv(file, pii_fields):
    """
    This function:
        looks in the passed-in file for 
          the given PII fields and 
          obfuscates the data under those
          fields.
    
    Arguments:
        file: the .csv file that previous 
          code has read from the S3 bucket.
        pii_filed: a list of strings, each
          string being a field in the .csv
          file.

    Returns:
        a byte stream in which code has 
          obfuscated the data under the 
          given PII fields.
    """


    input_stream = io.StringIO(file)
    reader = csv.DictReader(input_stream)

    output_stream = io.StringIO()
    writer = csv.DictWriter(output_stream, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        for field in pii_fields:
            row[field] = "***" if field in row else row.get(field)        
        writer.writerow(row)

    # Convert to byte stream
    return output_stream.getvalue().encode("utf-8")