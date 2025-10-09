def get_key_and_bucket_name(file_path_string):
    """
    This function:
        extracts the file name and the key
        from the passed-in string that
        represents the file path to the
        file in the S3 bucket.

    Args:
        a string that represents the file
        path to the file in the S3 bucket.

    Returns:
        a list of two members, each a
        string. The first string is the
        name of the S3 bucket and the
        second is the key under which the
        bucket stores the file.

    """

    parts_list = file_path_string.split("/")
    bucket_name = parts_list[2]
    key = parts_list[3] + "/" + parts_list[4]

    return [bucket_name, key]
