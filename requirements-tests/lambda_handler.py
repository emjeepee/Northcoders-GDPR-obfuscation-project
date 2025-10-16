import io
import csv
import random

from obf_lib import obfuscate

def lambda_handler(event, context):
    
    input = {
        'file_to_obfuscate': "s3://gdpr-obfus-my-ingestion-bucket-ga47fmw2/new_data/file1.csv" ,
        'pii_fields': ['name', 'email_address']
            }

    byt_str = obfuscate(input)

    # make byt_str a file-like object:
    byt_str_file = io.BytesIO(byt_str)        

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

    for i, row in enumerate(reader, start=1):
        if i == rand_line:
            print(f'This is row number {rand_line}:')
            print(f'{row}')
            break
    
    return {"statusCode": 200, "body": "All is well."}