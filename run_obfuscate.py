import io
import random
import sys
import json
import os
import csv

from obf_lib import obfuscate

def run_obfuscate():
    # Text colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    RESET = "\033[0m"  # Reset colour to default

    # print(RED + "This is red" + RESET)
    # print(GREEN + "This is green" + RESET)
    # print(YELLOW + "This is yellow" + RESET)
    # print(BLUE + "This is blue" + RESET)


    # show user an error message 
    # if the number of arguments 
    # to run_obfuscate.py is not 1:  
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
        # tell user that the input data
        # has been loaded successfully: 
        print(GREEN)
        print('****---***---****---***---****---***---****')
        print(YELLOW)
        print(f"\n\nInput successfully loaded from '{json_file_path}'")
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

    # get a random line from the
    # byte stream:

    # make byt_str a file-like object:
    byt_str_file = io.BytesIO(result)        
    # reset and wrap the byte stream:

    byt_str_file.seek(0)

    # wrap in a text stream
    text_stream = io.TextIOWrapper(byt_str_file, encoding="utf-8")

    # count lines (excluding header):
    line_count = sum(1 for _ in text_stream) - 1

    # pick a random line number:
    rand_line = random.randint(1, line_count)

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
    print(f"Here is a print out of the headers and \nup to five consecutive rows from the byte \nstream returned by function obfuscate() \nbeginning with randomly chosen row number \n{rand_line}. The obfuscated data appears under \nthe correct fields:")
    # join headers with commas for a neat single-line print
    print(PURPLE)
    print("          ".join(headers))
    print(BLUE)
    for i, row in enumerate(reader, start=1):
        if i == rand_line:
            print(f'{row['name']}             {row['email_address']}                  {row['age']}            {row['height']}           {row['weight']}     ROW {rand_line}') 
        if i == rand_line + 1:
            print(f'{row['name']}             {row['email_address']}                  {row['age']}            {row['height']}           {row['weight']}     ROW {rand_line+1}') 
        if i == rand_line + 2:
            print(f'{row['name']}             {row['email_address']}                  {row['age']}            {row['height']}           {row['weight']}     ROW {rand_line+2}') 
        if i == rand_line + 3:
            print(f'{row['name']}             {row['email_address']}                  {row['age']}            {row['height']}           {row['weight']}     ROW {rand_line+3}') 
        if i == rand_line + 4:
            print(f'{row['name']}             {row['email_address']}                  {row['age']}            {row['height']}           {row['weight']}     ROW {rand_line+4}') 
    
            break
    print(RESET)
run_obfuscate()