import boto, sys, os, yaml, zipfile, logging
from zipfile import ZipFile

class S3Download:



    def  __init__ (self,download_path,aws_access_key,aws_secret_access_key,bucket_name):
        self.log_file = os.path.join('d:/', 'data','import_logs','s3_log.txt')
        logging.basicConfig(filename=self.log_file,level=logging.DEBUG)
        bucket = self.connect_to_bucket(aws_access_key,
                                        aws_secret_access_key,
                                        bucket_name
                                        )
        self.download_zip_file(bucket, download_path)
        self.uncompress_file(download_path)

    def connect_to_bucket(self, access_key, secret_key, bucket):
        try:
            conn = boto.connect_s3(access_key, secret_key)
            return conn.get_bucket(bucket)
            logging.info('Connected to bucket')
        except Exception, e:
            logging.error('Failed Connection to bucket ' + e.message)


    def download_zip_file(self, bucket, download_path):
        try:
            file_list = [(k.last_modified, k) for k in bucket]
            key_to_download = sorted(file_list,
                                     cmp=lambda x,y: cmp(x[0], y[0])
                                     )[-1][1]
            return key_to_download.get_contents_to_filename(download_path)
            logging.info('Downloaded file')
        except Exception, e:
            logging.error('Failed to download file ' + e.message)

    def uncompress_file(self, file_path):
        try:
            zip_file = ZipFile(file_path)
            zip_file.extractall(os.path.join('d:/','data', 's3'))
            logging.info('Unziped file')
        except Exception, e:
            logging.error('Failed to uncompress file ' + e.message)