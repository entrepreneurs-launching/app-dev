import os
import boto3
import logging
from botocore.exceptions import ClientError

bucket_name = "helloamplify-trip-destination-image-storage164155-dev"

def download_file(bucket, object_name, file_name_save):
    s3_client = boto3.client('s3')
    try:
        s3_client.download_file(bucket, object_name, file_name_save)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_file(bucket, file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


"""
ret = upload_file(bucket_name, "file.pcap")
print (ret)
ret = download_file(bucket_name, "file.pcap", "file-down.pcap")
print (ret)

"""
