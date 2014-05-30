import os

class UpdateFiles:

    def __init__ (self):
        filepath='d:\\backup\\s3\\'
        target_directory = 'd:\\data\\'
        filegdb_name = 'WDPA_current.gdb'
        old_suffix = '_old'
        all_subdirs = self.all_subdirs_of(filepath)
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        old_filegdb_name = self.all_subdirs_of(latest_subdir)[0]
        os.renames(target_directory + filegdb_name, target_directory + filegdb_name + old_suffix)
        os.renames(old_filegdb_name, target_directory + filegdb_name)


    def all_subdirs_of(self, b='.'):
        result = []
        for d in os.listdir(b):
            bd = os.path.join(b, d)
            if os.path.isdir(bd): result.append(bd)
        return result




