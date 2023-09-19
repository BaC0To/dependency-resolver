from read_from_json import read_json_file
from list_of_dicts_to_single_dict import package_to_dict


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
        for i in input_dictionary[item]: # run the for loop to check the not visited nodes and then append the same from the visited and queue list.
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

if __name__ == "__main__":

    starting_node = "D"
    print(breadth_first_search(package_to_dict(read_json_file("package.JSON")), starting_node))
