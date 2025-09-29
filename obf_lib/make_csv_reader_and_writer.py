import io
import csv



def make_csv_reader_and_writer(file_content):
    """
    This function:
        creates a csv reader and writer
        from the passed-in string that is
        the contents of a csv file.
    
    Arguments:
        file_contents: a string that is the 
        contents of a csv file.

    Returns:
        A list the first member of which is 
        a csv reader and the second member 
        of which is a csv writer.
    
    
    """
    input_stream = io.StringIO(file_content)
    reader = csv.DictReader(input_stream)

    output_stream = io.StringIO()
    writer = csv.DictWriter(output_stream, fieldnames=reader.fieldnames)
    writer.writeheader()

    return [reader, writer]