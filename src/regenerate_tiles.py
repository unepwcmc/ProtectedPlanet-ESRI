import arcpy, sys
from arcpy import env
import os, sys, time, datetime, traceback, string, logging

class RegenerateTiles:


    def __init__(self,data_directory,connectionFile,server,serviceName):
        self.log_file = os.path.join('d:/', 'data','import_logs','tiles_log.txt')
        logging.basicConfig(filename=self.log_file,level=logging.DEBUG)
        inputService = connectionFile + "\\" + server + "\\" + serviceName
        scales = ""
        numOfCachingService = 2
        updateMode = "RECREATE_ALL_TILES"
        areaOfInterest = ""
        waitForJobCompletion = "WAIT"
        updateExtents = ""
        env.workspace = data_directory
        successfully_generated = self.manage_mapserver(serviceName,
                                                       inputService,
                                                       scales,
                                                       updateMode,
                                                       numOfCachingService,
                                                       areaOfInterest,
                                                       updateExtents,
                                                       waitForJobCompletion)
        print 'Tiles Updated Successfully' if successfully_generated \
        else 'Tiles Not Updated'


    def manage_mapserver(self,
                         serviceName, inputService,
                         scales, updateMode,numOfCachingService,
                         areaOfInterest, updateExtents, waitForJobCompletion):

        try:
            starttime = time.clock()
            result = arcpy.ManageMapServerCacheTiles_server(inputService,
                                                            scales,
                                                            updateMode,
                                                            numOfCachingService,
                                                            areaOfInterest,
                                                            updateExtents,
                                                            waitForJobCompletion
                                                            )
            finishtime = time.clock()
            elapsedtime= finishtime - starttime
            while result.status < 4:
                time.sleep(0.2)
            resultValue = result.getMessages()
            logging.info('Completed Tile Generation')
            return True

        except Exception, e:
            tb = sys.exc_info()[2]
            logging.error('Failed to uncompress file ' + e.message + tb.tb_lineno)

