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

visited = [] # declare empty list to store visited nodes

def depth_first_search(visited, start_node): 
     
    for i in list_dict_values:
            current_node = start_node
            #check if current dict has a key <item>
            if current_node == list(i.values())[0]:
                 # check+
                 new_vals = list(i.values())[1]
                 print(new_vals)
                 visited = visited + new_vals
                 print(visited)
                 print(f"Dict key: {list(i.values())[0]} and resp. value: {list(i.values())[1]}")
                 for i in visited[0]:
            
                    print(f"Here we must dig: {i}")
    return visited

if __name__ == "__main__":

    starting_node = "A"
    print(depth_first_search(visited, starting_node))