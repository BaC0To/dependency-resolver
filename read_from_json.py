import json
from pathlib import Path

def read_json_file(filename):
    """Function to read data from .json file
    param: filename
    return: data:dict
    """
    with Path(filename).open("r") as source:
        return json.load(source)

#if __name__ == '__main__':
    #print(read_json_file("package.JSON"))
