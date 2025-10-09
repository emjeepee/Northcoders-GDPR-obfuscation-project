
## Project title 

# GDPR-compliant obfuscation of PII data in a file  
<br>
<br>
<br>


## Description <br>
This project creates a Python library module that will obfuscate personally identifiable information (PII) stored under certain fields in a given file. <br> <br>
The calling procedure will supply this module with a json string that takes the following form:  <br>
```
"""
{
	"file_to_obfuscate": "s3://my_ingestion_bucket/new_data/file1.csv", 
	"pii_fields": ["name", "email"]
}
""" 
```
<br> <br>
The value of key "file_to_obfuscate" is a string representing a path to the file in an Amazon Web Services (AWS) S3 bucket and comprises these parts: <br>

 - __'my_ingestion_bucket'__ is the name of the S3 bucket. <br>
 - __'new_data/file1.csv'__ is the name of the key under which the S3 bucket stores the file. <br>
 - __'file1.csv'__ is the name of the file that contains fields, some of which have data to be obfuscated.<br><br>

The value of key "pii_fields" is a list of strings, each of which represents a field in file file1.csv whose data this module must obfuscate.
<br> <br>
This module obfuscates the data in file file1.csv under the specified PII fields then converts the file into a bytestream. This module then returns that bytestream.
<br> <br> <br>


## Project directories
This project includes the following main directories:
 - __obf_lib__ <br> this contains module main.py, which contains function obfuscate().
   Function obfuscate() calls several utility functions, all of which reside
   in modules in directory obf_lib. Each utility function resides in a module of the same name, for example function process_csv() resides in module process_csv.py. 
 - __tests__ <br> this contains test_\*.py files, where '\*' is the name of a function to test. An example file is test_process_csv().py, which contains the tests for the function process_csv().
 <br><br><br>



## Author
- Mukund Pandit <br>  __email__: mukund.panditman.googlemail.com

<br><br>



## Setup and use

Instructions for setup and use of this library:  <br>
- view this GitHub repository: https://github.com/emjeepee/Northcoders-GDPR-obfuscation-project
- find directory obf_lib in that repository and copy that directory into your project
- then import the library into a Lambda handler function or any module in your project where you want to use it, like this:
  <br>
```
from <path.to.directory.obf_lib> import obfuscate
```

- example use of the library in a Lambda handler Python function or any Python module:
```
from <path.to.directory.obf_lib> import obfuscate

json_input = '{"file_to_obfuscate": "s3://bucket_name_here/key_name/file.csv", "pii_fields": ["name", "email"]}'

# obf_byte_stream below contains a byte stream 
# version of file file.csv but with data under 
# the fields name and email obfuscated with '***':
obf_byte_stream = obfuscate(json_input)
```

 <br><br>







## Tech Stack

 - Code: Python 3.13.2
 - Built-in Python modules json, io, csv, os 
 - Other Python modules: boto3
 - Built-in Python testing modules: unittest
 - Other Python testing modules: pytest, moto 
  <br><br><br>



## Compatibility with Python versions

This project used command-line automation tool __tox__ to test the code's compatibility across various versions of Python.  <br>
Tool __tox__ showed that the code is compatible with the following stable versions of Python: <br> 
 - 3.9.24
 - 3.10.18
 - 3.11.13
 - 3.12.12
 - 3.13.2

  <br><br><br>






## Testing of the code

### To test all functions in this library <br>

- clone this GitHub repository: https://github.com/emjeepee/Northcoders-GDPR-obfuscation-project <br>
- from the command line navigate to the top-most directory of the cloned project  <br>
- either directly in the top-most directory or inside a virtual environment created in the top-most directory install modules moto and pytest by running the following in the command line:  <br>
```pip install pytest``` 
and   <br> 
```pip install moto```  <br>
- Then run the following in the command line:  <br>
```pytest -vvvrP```
<br><br>




### Test coverage <br>

Running command-line tool __coverage__ and generating a report produces the following output, which shows that on average the tests have covered 97% of the code in this project. Here is the output:

```
Name                                       Stmts   Miss  Cover   Missing
------------------------------------------------------------------------
obf_lib/__init__.py                            1      0   100%
obf_lib/deal_with_csv.py                       8      0   100%
obf_lib/deal_with_json.py                      4      1    75%   30
obf_lib/deal_with_parquet.py                   3      1    67%   29
obf_lib/find_input_type.py                     6      0   100%
obf_lib/func_lookup.py                         4      0   100%
obf_lib/get_file.py                            6      0   100%
obf_lib/get_key_and_bucket_name.py             5      0   100%
obf_lib/main.py                               11      0   100%
obf_lib/make_csv_reader_and_writer.py          9      0   100%
obf_lib/process_csv.py                         7      0   100%
obf_lib/process_json.py                        2      1    50%   20
obf_lib/return_data_type.py                    4      0   100%
tests/test_deal_with_csv.py                   20      0   100%
tests/test_find_input_type.py                 14      0   100%
tests/test_get_file.py                        35      5    86%   14-18
tests/test_get_key_and_bucket_name.py         26      0   100%
tests/test_make_csv_reader_and_writer.py      33      1    97%   22
tests/test_obfuscate.py                       38      0   100%
tests/test_process_csv.py                     35      0   100%
tests/test_return_data_type.py                36      0   100%
------------------------------------------------------------------------
TOTAL                                        307      9    97%

```
<br>
The modules that show less than the industry-standard 90% coverage are: <br>

 - obf_lib/deal_with_json.py  <br>
 - obf_lib/deal_with_parquet.py  <br>
 - obf_lib/process_json.py   <br>
These modules contain only stubbs of functions as they are not required for the MVP. <br><br>
 - tests/test_get_file.py and tests/test_make_csv_reader_and_writer.py. <br> 
These are test files used by command-line tool pytest and their less-than-90% coverage figures are of no consequence.<br>


  <br><br><br>





## Test for security vulnerabilities <br>

### Static code analysis: <br>

Running command-line tool __bandit__ recursively on directory __obf_lib__ showed that the code has no security issues at any severity level and nothing that __bandit__ suspected might be insecure.<br>

This is the output of  __bandit__: <br>
```
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.13.2
Run started:2025-10-08 14:22:01.582822

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 306
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 0
Files skipped (0):
```

 <br> 


<br> 

## PEP8 compliance <br>
This project ran command-line tool __black__ recursively on directory obf_lib to ensure PEP8 compliance of the code. <br>
This project also ran command-line tool __flake8__ to test for <br>

 - consistency of code style
 - avoidance of complexity
 - simple bugs

 <br> 
The ouput of flake8 follows: <br> 

```
obf_lib/__init__.py:1:1: F401 '.main.obfuscate' imported but unused
obf_lib/deal_with_json.py:1:1: F401 'obf_lib.get_file.get_file' imported but unused
obf_lib/deal_with_json.py:2:1: F401 'obf_lib.process_json.process_json' imported but unused
obf_lib/deal_with_parquet.py:1:1: F401 'obf_lib.get_file.get_file' imported but unused
```  
<br> 
Explanation of why the flake8 warnings are not of concern: <br>

- module obf_lib/__init__.py must import main.obfuscate to allow the library to be used as a library. __init__.py is not meant to employ funtion main.obfuscate.  
- modules obf_lib/deal_with_json.py and obf_lib/deal_with_parquet.py contain only stubbs of functions. This project does not employ those functions and those functions are not part of the MVP.

<br><br>


