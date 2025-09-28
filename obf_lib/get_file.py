import boto3




def get_file(bucket: str, key: str):
    """
    This function:
        reads the S3 bucket and gets
        the file stored there under 
        a given key.
    
    Args:
        bucket: a string that is the 
          name of the bucket.
        key: a string that is the key
          under which the S3 bucket stores 
          the file that contains the data, 
          some of which will be 
          obfuscated in a different
          function.

    Returns:
        The file that the S3 bucket bucket  
        stores under key key.
    """
    

    s3_client = boto3.client("s3")
    objct = s3_client.get_object(Bucket=bucket, Key=key)
    file = objct["Body"].read().decode("utf-8")
    
    return file