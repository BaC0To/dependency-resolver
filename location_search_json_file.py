import os
from pathlib import Path


def json_location_finder():
    """Function that searches for a .JSON file in the project filestructure
    return filepath: class pathlib.WindowsPath
    """
    FILENAME_EXT = ".JSON"

    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            (base, ext) = os.path.splitext(name) # split base and extension 
            if ext == FILENAME_EXT:
                full_path_and_name = os.path.join(root, name) # create full path
                return Path(full_path_and_name)
            

if __name__ == "__main__":
    print(json_location_finder())
