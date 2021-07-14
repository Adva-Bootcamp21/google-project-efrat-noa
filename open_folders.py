import os
from zipfile import ZipFile
import urllib.request


class OpenFolders:
    def __init__(self, folder_path):
        self.__folder_path = folder_path
        self.__files = []

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.__files):
            res = open(self.__files[self.i - 1], encoding="utf8")
            res = res.readlines()
            self.i += 1
            return res
        else:
            raise StopIteration

    def create_list(self, path):
        # create a list of file and sub directories
        # names in the given directory
        list_of_file = os.listdir(path)
        self.__files = list()
        # Iterate over all the entries
        for entry in list_of_file:
            # Create full path
            full_path = os.path.join(path, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(full_path):
                self.create_list(full_path)
            else:
                self.__files.append(full_path)
        return self.__files

# archive = OpenFolders("./2021-archive")
# archive.create_list("./2021-archive")
