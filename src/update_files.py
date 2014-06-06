import os, arcpy, shutil
from arcpy import env


class UpdateFiles:

    def __init__ (self):

        target_directory = 'd:\\data\\'
        download_path = target_directory + 's3\\'
        current_filegdb_name = 'WDPA_current.gdb'
        old_suffix = '_old'

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
        return [os.path.join(directory, name) for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]

    def latest_subdir(self, all_subdirs):
        return max(all_subdirs, key=os.path.getmtime)


    def feature_name(self, name):
        feature_classes = arcpy.ListFeatureClasses()
        return filter(lambda x:name in x, feature_classes)

    def change_table_name(self, table, geometry_type):
        print table
        return arcpy.Rename_management(table, 'WDPA_' + geometry_type)







