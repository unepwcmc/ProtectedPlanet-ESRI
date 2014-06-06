import os, arcpy, shutil, logging, sys
from arcpy import env


class UpdateFiles:

    def __init__ (self):

        target_directory = 'd:\\data\\'
        download_path = target_directory + 's3\\'
        current_filegdb_name = 'WDPA_current.gdb'
        old_suffix = '_old'
        self.log_file = os.path.join('d:/', 'data','import_logs','files_log.txt')
        logging.basicConfig(filename=self.log_file,level=logging.DEBUG)
        download_subdirs = self.all_subdirs_of(download_path)
        latest_download = self.latest_subdir(download_subdirs)
        filegdb_full_path = self.all_subdirs_of(latest_download)[0]
        env.workspace = filegdb_full_path
        poly_table = self.feature_name('WDPApoly')[0]
        point_table = self.feature_name('WDPApoint')[0]
        self.change_table_name(poly_table, 'poly')
        self.change_table_name(point_table, 'point')
        shutil.rmtree(target_directory + current_filegdb_name + old_suffix)
        os.renames(target_directory + current_filegdb_name,
                   target_directory + current_filegdb_name + old_suffix)
        os.renames(filegdb_full_path, target_directory + current_filegdb_name)

    def all_subdirs_of(self,directory):
        try:
            return [os.path.join(directory, name)
                    for name in os.listdir(directory)
                    if os.path.isdir(os.path.join(directory, name))]
        except Exception, e:
            tb = sys.exc_info()[2]
            logging.error('Failed to get subdirectories ' + e.message
                          + tb.tb_lineno)

    def latest_subdir(self, all_subdirs):
        try:
            return max(all_subdirs, key=os.path.getmtime)
        except Exception, e:
            tb = sys.exc_info()[2]
            logging.error('Failed to get latest subdirectory ' + e.message
                          + tb.tb_lineno)


    def feature_name(self, name):
        try:
            feature_classes = arcpy.ListFeatureClasses()
            return filter(lambda x:name in x, feature_classes)
        except Exception, e:
            tb = sys.exc_info()[2]
            logging.error('Failed to get feature name ' + e.message
                          + tb.tb_lineno)

    def change_table_name(self, table, geometry_type):
        try:
            print table
            return arcpy.Rename_management(table, 'WDPA_' + geometry_type)
        except Exception, e:
            tb = sys.exc_info()[2]
            logging.error('Failed to change table name ' + e.message
                          + tb.tb_lineno)






