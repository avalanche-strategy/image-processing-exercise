import boto3

def get_s3_client():
    s3 = boto3.client('s3',
                  endpoint_url="http://localstack:4572",
                  use_ssl=False,
                  aws_access_key_id='ACCESS_KEY',
                  aws_secret_access_key='SECRET_KEY',
                  region_name='us-east-1')

    # Create a bucket to store images in
    s3.create_bucket(Bucket='images')

    return s3