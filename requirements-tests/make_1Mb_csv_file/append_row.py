import csv





def append_row(file_path, row):
    with open(file_path, 'a', newline = '') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(row)