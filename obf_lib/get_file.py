import boto3




def get_file(bucket: str, key: str):
    """
    This function:
        reads the S3 bucket, gets the 
        file stored there under the 
        given key, converts the contents 
        of the file to a string and 
        returns the string.
    
    Args:
        bucket: a string that is the 
          name of the S3 bucket.
        key: a string that is the key
          under which the S3 bucket stores 
          the file that contains the data, 
          some of which will be 
          obfuscated in a different
          function.

    Returns:
        A string that is the contents of 
        the file that the given S3 bucket 
        stores under the given key.
    """
    

    s3_client = boto3.client("s3")
    objct = s3_client.get_object(Bucket=bucket, Key=key)
    file_content = objct["Body"].read().decode("utf-8")
    
    return file_content