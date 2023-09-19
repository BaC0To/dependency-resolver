import json


def get_json_data(json_file):
    """Function to read data from .json file
    param: filename
    return: data:dict
    """
    with open(json_file, "r") as file:
        return json.load(file)
    
def package_to_dict(json_data_in):
    """Function to convert all json data to a single dictionary
    param: json_data_in as ???
    return: dict
    """
    keys_list = []
    values_list = []

    for item in json_data_in.get("packages"):
        keys_list.append(item.get("name"))
        values_list.append(item.get("requires"))
        
    return dict(zip(keys_list, values_list))

def breadth_first_search(input_dictionary, start_node):
    """Function that visits all nodes of the three graph represented by the dictionary
    params : input_dictionary:dict, start_node: str
    return : all visited nodes with their dependancies:list
    """
    visited=[]
    stack=[]
    visited.append(start_node)
    stack.append(start_node)
    
    while stack:
        s = stack.pop(0)
        for x in input_dictionary[s]:
            if x not in visited:
                visited.append(x)
                stack.append(x)
    return visited

visited = []

def depth_first_search(visited, dictionary, node): 
    if node not in visited:
        visited.append(node)
        for x in dictionary[node]:
            depth_first_search(visited, dictionary, x)
    return visited


#all_data = get_json_data("package.JSON")
print(breadth_first_search(package_to_dict(get_json_data("package.JSON")), "A"))
