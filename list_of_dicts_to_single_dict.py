import json
import os
from pathlib import Path


REPO_ROOT = Path(os.getcwd())
CONFIG_DIR = Path("config_files")
JSON_FILE_PATH = os.path.join(REPO_ROOT, CONFIG_DIR, "package.JSON")


with open(JSON_FILE_PATH,"r") as source:
    data_json = json.load(source)
    
#print(data_json)
list_dict_values = data_json["packages"]
#print(list_dict_values)

def package_to_dict(json_data_in):
    
    keys_list = []
    values_list = []

    for item in json_data_in.get("packages"):# get 1st value from .json dict
        keys_list.append(item.get("name"))# get values from key "name" : "value_X" for all listed dicts and append it in keys_list
        values_list.append(item.get("requires"))# get values from key "requires" : "value_X" for all listed dicts and append it in values_list
        
    return dict(zip(keys_list, values_list))# create new simple dict from keys/values_list

if __name__ == "__main__":
    
    print(package_to_dict(data_json))

