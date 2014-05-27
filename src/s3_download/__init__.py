import boto
import sys, os
import yaml
import zipfile
from zipfile import ZipFile

s3_secrets_file = open(os.path.join('src', 'config','s3.yaml'),'r')
s3_secrets = yaml.load(s3_secrets_file)


FILE_PATH = 'd:\\backup\\s3\\current_wdpa.zip'
AWS_ACCESS_KEY_ID = s3_secrets['access_key_id']
AWS_SECRET_ACCESS_KEY = s3_secrets['secret_access_key']
bucket_name = s3_secrets['bucket_name']
# connect to the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)
# go through the list of files
file_list = [(k.last_modified, k) for k in bucket]
key_to_download = sorted(file_list, cmp=lambda x,y: cmp(x[0], y[0]))[-1][1]
key_to_download.get_contents_to_filename(FILE_PATH)
zip_file = ZipFile(FILE_PATH)
zip_file.extractall('d:\\backup\\s3\\')