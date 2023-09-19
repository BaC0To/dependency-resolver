#from read_from_json import read_json_file
from list_of_dicts_to_single_dict import package_to_dict
import json
import os
from pathlib import Path


REPO_ROOT = Path(os.getcwd())
CONFIG_DIR = Path("config_files")
JSON_FILE_PATH = os.path.join(REPO_ROOT, CONFIG_DIR, "package.JSON")


with open(JSON_FILE_PATH,"r") as source:
    data_json = json.load(source)
    
list_dict_values = data_json["packages"]


def breadth_first_search(input_dictionary, start_node):
    """Function that keeps appending the visited and queued nodes
    params : input_dictionary:dict, start_node: str
    return : all visited nodes with their dependancies:list
    """

    visited=[] # declare empty list to store visited nodes
    queue=[] # declare empty list to store nodes in the queue
    visited.append(start_node)
    queue.append(start_node)
    
    while queue: #  run the while loop for the queue for visiting the nodes and then will remove the same node and print it as it is visited.
        item = queue.pop(0)
        vals = input_dictionary[item]
        for i in input_dictionary[item]: # run the for loop to check the not visited nodes and then append the same from the visited and queue list.
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited


if __name__ == "__main__":

    starting_node = "B"
    print(breadth_first_search(package_to_dict(data_json), starting_node))
 