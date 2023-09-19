import json
from location_search_json_file import json_location_finder


def read_json_file():
    """Function to read data from .json file
    param: filename
    return: data:dict
    """
    with open(json_location_finder(),"r") as source:
        return json.load(source)


if __name__ == "__main__":
    print(read_json_file())