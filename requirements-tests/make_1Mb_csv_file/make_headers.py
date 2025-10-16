import csv




def make_headers(file_path):
    # NOTE: file_path has to be relative to where you run
    # python make_headers.py from.

    headers = ['name', 'email_address', 'age', 'height', 'weight']
    # NOTE: you have to use 'w' as second arg below 
    # as it means 'write'. If you omit it the open()
    # defaults to 'r' for 'read' and the function fails:
    with open(file_path, 'w', newline='') as csvf:
        csv_writer = csv.writer(csvf)
        csv_writer.writerow(headers)


    
# make_headers('data/file1.csv')