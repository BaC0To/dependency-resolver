import os
from pathlib import Path

FILENAME_EXT = ".JSON"

def json_location_finder(file_name_ext):
    """
    Function that searches for a .JSON file in the project filestructure
    param: file_name_ext: str
    return filepath: class pathlib.WindowsPath
    """
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(file_name_ext):
                path = Path(filepath)
                return path
            

""" if __name__ == "__main__":
    print(json_location_finder(FILENAME_EXT))
"""