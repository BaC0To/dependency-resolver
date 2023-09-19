from read_from_json import read_json_file
from list_of_dicts_to_single_dict import package_to_dict


visited = [] # declare empty list to store visited nodes

def depth_first_search(visited, input_dictionary, start_node): 
    if start_node not in visited:
        visited.append(start_node)
        for x in input_dictionary[start_node]:
            depth_first_search(visited, input_dictionary, x)
    return visited

if __name__ == "__main__":

    starting_node = "A"
    print(depth_first_search(visited, package_to_dict(read_json_file()), starting_node))