import os
from pathlib import Path
import json


REPO_ROOT = Path(os.getcwd())
CONFIG_DIR = Path("config_files")
JSON_FILE_PATH = os.path.join(REPO_ROOT, CONFIG_DIR, "package.JSON")


with open(JSON_FILE_PATH,"r") as source:
    data_json = json.load(source)
    
#print(data_json)
list_dict_values = data_json["packages"]
#print(list_dict_values)

""" for i in list_dict_values:
    print(i.keys())
    print(i.values())
    print(f"Dict key: {list(i.values())[0]} and resp. value: {list(i.values())[1]}") """

def bfs_search(start_node):
    """Function that keeps appending the visited and queued nodes usign BFS algorithm
    params : start_node: str
    return : all visited nodes with their dependancies: list
    """
     # declare empty list to store visited nodes
    visited=[]
     # declare empty list to store nodes in the queue
    queue=[]
    visited.append(start_node)
    queue.append(start_node)
    
    while queue:
        item = queue.pop(0)
         # i == current dict from list dict
        for i in list_dict_values:
            #check if current dict has a key <item>
            if item == list(i.values())[0]: 
                #vals = list(i.values())[1]
                for j in list(i.values())[1]:
                    if j not in visited:
                        visited.append(j)
                        queue.append(j)
    return visited


if __name__ == "__main__":

    starting_node = "C"
    print(bfs_search(starting_node))
    #print(data_json)