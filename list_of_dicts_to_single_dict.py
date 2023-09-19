from read_from_json import read_json_file
       
def package_to_dict(json_data_in):
    """Function to convert all json data to a single dictionary
    param: json_data_in as dict
    return: dict
    """
    keys_list = []
    values_list = []

    for item in json_data_in.get("packages"):# get 1st value from .json dict
        keys_list.append(item.get("name"))# get values from key "name" : "value_X" for all listed dicts and append it in keys_list
        values_list.append(item.get("requires"))# get values from key "requires" : "value_X" for all listed dicts and append it in values_list
        
    return dict(zip(keys_list, values_list))# create new simple dict from keys/values_list

""" if __name__ == "__main__":
    print(package_to_dict(read_json_file()))
 """