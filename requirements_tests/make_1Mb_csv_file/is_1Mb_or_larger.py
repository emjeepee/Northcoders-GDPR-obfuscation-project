import os


def is_1Mb_or_larger(file_path):
    file_size_bytes = os.path.getsize(file_path)
    
    if file_size_bytes > 1048576:
        print(f'The file size is {file_size_bytes} bytes')
        return True
    
    # print('The file is smaller than 1Mb')
    return False


# is_1Mb_or_larger('data/file1.csv')