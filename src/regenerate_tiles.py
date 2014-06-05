import arcpy, sys
from arcpy import env
import os, sys, time, datetime, traceback, string

class RegenerateTiles:


    def __init__(self):
        connectionFile = r"C:\Users\administrator\AppData\Roaming\ESRI\Desktop10.1\ArcCatalog"
        server = "arcgis on localhost_6080 (admin)"
        serviceName = "wdpa/wdpa.MapServer"
        inputService = connectionFile + "\\" + server + "\\" + serviceName
        scales = ""
        numOfCachingServiceInstances = 2
        updateMode = "RECREATE_ALL_TILES"
        areaOfInterest = ""
        waitForJobCompletion = "WAIT"
        updateExtents = ""
        env.workspace = "d:\data"
        current_time = self.current_time()
        print current_time
        report_location = os.path.join('d:/', 'data/')
        report = self.report_file(current_time[0], report_location)
        successfully_generated = self.manage_mapserver(current_time[1], report, serviceName, inputService, scales, updateMode,numOfCachingServiceInstances,areaOfInterest, updateExtents, waitForJobCompletion)
        print 'Tiles Updated Successfully' if successfully_generated else 'Tiles Not Updated'

    def current_time(self):
        currentTime = datetime.datetime.now()
        arg1 = currentTime.strftime("%H-%M")
        arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
        return [arg1,arg2]


    def report_file(self, current_time, report_file_location):
        file_name = r'report_%s.txt' % current_time
        report_file = report_file_location + file_name
        report = open(report_file,'w')
        return report

    def manage_mapserver(self, current_time, report, serviceName, inputService, scales, updateMode,numOfCachingServiceInstances,areaOfInterest, updateExtents, waitForJobCompletion):

        try:
            starttime = time.clock()
            result = arcpy.ManageMapServerCacheTiles_server(inputService,
                                                            scales,
                                                            updateMode,
                                                            numOfCachingServiceInstances,
                                                            areaOfInterest,
                                                            updateExtents,
                                                            waitForJobCompletion)
            finishtime = time.clock()
            elapsedtime= finishtime - starttime
            while result.status < 4:
                time.sleep(0.2)
            resultValue = result.getMessages()
            report.write ("completed " + str(resultValue))

            print "Created cache tiles for given schema successfully for "
            serviceName + " in " + str(elapsedtime) + " sec \n on " + current_time
            return True

        except Exception, e:
            # If an error occurred, print line number and error message
                tb = sys.exc_info()[2]
                report.write("Failed at step 1 \n" "Line %i" % tb.tb_lineno)
                report.write(e.message)
                report.close()
                return False

        print "Created Map server Cache Tiles "