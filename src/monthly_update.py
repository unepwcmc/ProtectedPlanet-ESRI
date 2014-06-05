import regenerate_tiles, s3_download, update_files
try:
    s3_download.S3Download
    print 'Downloaded from S3'

except Exception, e:
    print 'Download Failed'

try:
    update_files.UpdateFiles
    print 'Updated files'
except Exception, e:
    print 'Update Failed'

try:
    regenerate_tiles.RegenerateTiles
    print 'Generated Tiles'
except Exception, e:
    print 'Tile generation failed'