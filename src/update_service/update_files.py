import os
class UpdateFiles:

    def __init__ (self):
        filepath='d:\\backup\\s3\\'
        all_subdirs = self.all_subdirs_of(filepath)
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        return latest_subdir

    def all_subdirs_of(self, b='.'):
        result = []
        for d in os.listdir(b):
            bd = os.path.join(b, d)
            if os.path.isdir(bd): result.append(bd)
        return result
