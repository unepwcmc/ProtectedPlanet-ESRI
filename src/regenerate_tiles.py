import arcpy, sys
from arcpy import env
import os, sys, time, datetime, traceback, string

class RegenerateTiles:


    def __init__(self):


        server = "localhost"
        service = "wdpa/wdpa"
        dataFrame = ""
        inputLayers = ""
        extent = ""
        tiling_scheme = 'ARCGISONLINE_SCHEME'
        scales = "591657527.591555;295828763.79577702;147914381.89788899;73957190.948944002;36978595.474472001;18489297.737236001;9244648.8686180003;4622324.4343090001;2311162.2171550002"
        updateMode = "Recreate All Tiles"
        threadCount = "2"
        antialiasing = "NONE"
        pathToFeatureClass = ""
        ignoreStatus = ""
        tile_format = 'PNG'

# These lines run the update tool
        currentTime = datetime.datetime.now()
        arg1 = currentTime.strftime("%H-%M")
        arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
        file = 'C:/data/report_%s.txt' % arg1

# print results of the script to a report
        report = open(file,'w')
        try:
            starttime = time.clock()
            print 'Starting Cache Update'
            result = arcpy.ManageMapServerCacheTiles_server(server, service, dataFrame,
                                           inputLayers, tiling_scheme, scales, updateMode, antialiasing, pathToFeatureClass,ignoreStatus, tile_format)
            finishtime = time.clock()
            elapsedtime= finishtime - starttime
            while result.status < 4:
                time.sleep(0.2)
            resultValue = result.getMessages()
            report.write ("completed " + str(resultValue))

            print "Created cache tiles for given schema successfully for "
            + service + " in " + str(elapsedtime) + " sec \n on " + arg2

        except Exception, e:
            # If an error occurred, print line number and error message
            tb = sys.exc_info()[2]
            report.write("Failed at step 1 \n" "Line %i" % tb.tb_lineno)
            report.write(e.message)
            report.close()

        print "Created Map server Cache Tiles "