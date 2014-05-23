import boto
import sys, os
import yaml

s3_secrets_file = open(os.path.join('src', 'config','s3.yaml'),'r')
s3_secrets = yaml.load(s3_secrets_file)

LOCAL_PATH = 'd:\\backup\\s3\\'
AWS_ACCESS_KEY_ID = s3_secrets['access_key_id']
AWS_SECRET_ACCESS_KEY = s3_secrets['secret_access_key']

bucket_name = 'wdpa'
# connect to the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)
# go through the list of files
bucket_list = bucket.list()
for l in bucket_list:
    keyString = str(l.key)
    # check if file exists locally, if not: download it
    if not os.path.exists(LOCAL_PATH+keyString):
        l.get_contents_to_filename(LOCAL_PATH+keyString)
