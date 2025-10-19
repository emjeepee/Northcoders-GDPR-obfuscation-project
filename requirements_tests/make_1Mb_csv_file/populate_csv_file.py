from .make_headers import make_headers
from .is_1Mb_or_larger import is_1Mb_or_larger
from .append_row import append_row
from .make_row import make_row



def populate_csv_file(file_path):
    """
    This function:
        1) gets the file at the passed-in file path 
        and puts a table in it in the form of 
        comma separated values. The table has 
        the headers name, email_address, age, 
        height and weight. 
        2) populates the table with data under those 
        headers. The data consists of random 
        strings and numbers. 
        3) adds enough data such that the size of the
        file becomes approximately 1Mb. 
    
    Arguments:
        file_path: a string that is the path to 
        the empty file file1.csv

    Returns:
        None
   
    """
    
    # create the headings
    make_headers(file_path)

    while not is_1Mb_or_larger(file_path):
        row = make_row()
        append_row(file_path, row)

            




populate_csv_file('requirements-tests/data/file1.csv')    
    
   
