import os
import arcpy
from arcpy import env


class UpdateFiles:

    def __init__ (self):

        target_directory = 'd:\\data\\'
        download_path = target_directory + 's3\\'
        current_filegdb_name = 'WDPA_current.gdb'
        old_suffix = '_old'

        download_subdirs = self.all_subdirs_of(download_path)
        latest_download = self.latest_subdir(download_subdirs)
        filegdb_name = self.all_subdirs_of(latest_download)[0]
        env.workspace = download_path + filegdb_name
        poly_table = self.feature_name('WDPA_poly')
        point_table = self.feature_name('WDPA_point')
        self.change_table_name(poly_table, 'poly')
        self.change_table_name(point_table, 'point')

        os.renames(target_directory + current_filegdb_name, target_directory + current_filegdb_name + old_suffix)
        os.renames(download_path + filegdb_name, target_directory + filegdb_name)



    def all_subdirs_of(self, b='.'):
        result = []
        for d in os.listdir(b):
            bd = os.path.join(b, d)
            if os.path.isdir(bd): result.append(bd)
        return result

    def latest_subdir(self, all_subdirs):
        return max(all_subdirs, key=os.path.getmtime)


    def feature_name(self, name):

        feature_classes = arcpy.ListFeatureClasses()
        debugger
        print name
        return filter(lambda x:name in x, feature_classes)[0]

    def change_table_name(self, table, geometry_type):
        return arcpy.Rename_management(table, 'WDPA_' + geometry_type)







