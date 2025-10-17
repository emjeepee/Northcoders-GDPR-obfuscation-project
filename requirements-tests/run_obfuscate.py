import io
import random
import sys
import json
import os
import csv

from obf_lib import obfuscate





def run_obfuscate():
    '''
    This function:
        1) demonstrates the use of library
         obf_lib (specifically the library's 
         function obfuscate()).
         The user should run the following in 
         the command line:
         python run_obfuscate.py input.json
         where input.json is a file in the
         same directory as this module and 
         contains a dictionary that takes
         a form similar to this:
          {
  "file_to_obfuscate": "s3://my-ingestion-bucket/new_data/file1.csv",
  "pii_fields": ["name", "email_address"]  
          }. 
        The value of key "file_to_obfuscate"
        must be a string that is a 
        boto3-recognisable path to a .csv 
        file in an S3 bucket. The file must 
        contain headers and data below those 
        headers.
        The file must be saved under the key 
        new_data/file1.csv.
        Replace 'my-ingestion-bucket' with the 
        actual name of the S3 bucket.
        The value of key "pii_fields" is a list
        of the headers in the file below which 
        personably identifiable information must
        be obfuscated by function obfuscate(). 
        2) displays in the command line either:
            i)  the result of the use of function 
                obfuscate(). The display shows
                the headers in the bytestream that
                obfuscate() returns and 10 randomly 
                selected rows from the bytestream
            ii) error messages if, for example, 
                the user has not provided an 
                argument to the command line 
                command

    Arguments:
        none

    Returns:
        None                 

    '''


    # Text colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    RESET = "\033[0m"  # Reset colour to default

    # show user an error message 
    # if in the command line the number of 
    # arguments to command 
    # python run_obfuscate.py 
    # is not 1. the argument must be a 
    # .json file):  
    if len(sys.argv) != 2: # the first arg is run_obfuscate.py, hence '2' in this line
        print(RED + "\n \nIncorrect number of arguments to" + YELLOW + " run_obfuscate.py\n" + RESET)
        print(RED + "Run this in the command line: " + YELLOW + "\nrun_obfuscate.py <path_to_json_file>\n" + RESET)
        print(YELLOW + "For example: \npython run_obfuscate.py input.json\n \n \n" + RESET)
        sys.exit(1)

    # grab the file path to the 
    # .json file:
    json_file_path = sys.argv[1]

    # check whether file exists:
    if not os.path.isfile(json_file_path):
        print(RED)
        print(f"\n \n File '{json_file_path}' not found! \n \n")
        print(RESET)
        sys.exit(1)

    # get the json data out of the 
    # JSON file:
    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            input_data = json.load(f)
            pii_fileds = input_data['pii_fields']
        # tell user that the input data
        # has been loaded successfully: 
        print(GREEN)
        print('****---***---****---***---****---***---****')
        print(RESET)
            
    except json.JSONDecodeError as e:
        print(RED)
        print(f"\n\nInvalid JSON in file '{json_file_path}'. Ensure the file contains json and has a .json suffix.\n\n")
        print(RESET)
        sys.exit(1)

    # call obfuscate():
    try:
        result = obfuscate(input_data)
    except Exception as e:
        print(RED)
        print(f"\nThere was an error while running obfuscate(). \n")
        print(YELLOW)
        print(f"Check your AWS credentials, the name of the S3\nbucket and key under which the .csv file resides\nin the S3 bucket.")
        print(f"\nAlso check the values of the keys in the .json file\n\n\n")                
        print(RESET)
        sys.exit(1)

    # make byt_str a file-like object:
    byt_str_file = io.BytesIO(result)        
    # reset and wrap the byte stream:

    byt_str_file.seek(0)

    # wrap in a text stream
    text_stream = io.TextIOWrapper(byt_str_file, encoding="utf-8")

    # count lines (excluding header):
    line_count = sum(1 for _ in text_stream) - 1

    # pick 10 unique random line numbers
    # and sort them:
    rand_lines = random.sample(range(1, line_count + 1), 10)
    rand_lines = sorted(rand_lines)

    # rewind stream
    text_stream.seek(0)    # reset stream and read again:
    
    reader = csv.DictReader(text_stream)

    # report result type and size, 
    # headers and a random line from the 
    # byte stream:
    # Print header names (fieldnames) before printing the chosen row
    headers = reader.fieldnames
    print(GREEN)
    print('****---***---****---***---****---***---****')
    print('')
    print(f"\nFunction obfuscate() of library obf_lib \nreturned a byte stream of length \n{len(result)} bytes.")
    print(YELLOW)
    print(f"Below is a printout of the headers and \n10 random rows from the byte stream \nreturned by function obfuscate() of \nlibrary obf_lib. It shows that the \nobfuscated data appears under the \ncorrect fields. You chose to obfuscate \ndata under these fields \n{pii_fileds}:")
    # join headers with commas for a neat single-line print
    print(PURPLE)
    print("          ".join(headers))
    print(BLUE)
    for i, row in enumerate(reader, start=1):
        if i in rand_lines:
            row_values = "               ".join(str(row[field]) for field in reader.fieldnames)
            print(f"{row_values}             ROW {i}")    
    print(RESET)






run_obfuscate()