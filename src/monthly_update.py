import regenerate_tiles, s3_download, update_files,boto,yaml,os

s3_secrets_file = open(os.path.join('config','s3.yaml'),'r')
s3_secrets = yaml.load(s3_secrets_file)
download_path = os.path.join('d:/', 'data', 's3', 'new_wdpa.zip')
aws_access_key = s3_secrets['access_key_id']
aws_secret_access_key = s3_secrets['secret_access_key']
bucket_name = s3_secrets['bucket_name']
data_directory = 'd:\\data\\'
connectionFile = r"C:\Users\administrator\AppData\Roaming\ESRI\Desktop10.1\ArcCatalog"
server = "arcgis on localhost_6080 (admin)"
serviceName = "wdpa/wdpa.MapServer"

try:
    s3_download.S3Download(download_path,aws_access_key,aws_secret_access_key,bucket_name)
    print 'Downloaded from S3'

except Exception, e:
    print 'Download Failed'

try:
    update_files.UpdateFiles(data_directory)
    print 'Updated files'
except Exception, e:
    print 'Update Failed'

try:
    regenerate_tiles.RegenerateTiles(data_directory,connectionFile,server,serviceName)
    print 'Generated Tiles'
except Exception, e:
    print 'Tile generation failed'