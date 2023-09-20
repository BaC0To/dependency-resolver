import os
from pathlib import Path
import json


REPO_ROOT = Path(os.getcwd())
CONFIG_DIR = Path("config_files")
JSON_FILE_PATH = os.path.join(REPO_ROOT, CONFIG_DIR, "package.JSON")


with open(JSON_FILE_PATH,"r") as source:
    data_json = json.load(source)


def bfs_search(start_node):
    """Function that keeps appending the visited and queued nodes usign BFS algorithm
    params : start_node: str
    return : all visited nodes with their dependancies: list
    """
     # declare empty list to store visited nodes
    visited_from_bfs=[]
     # declare empty list to store nodes in the queue
    queue=[]
    visited_from_bfs.append(start_node)
    queue.append(start_node)
    
    while queue:
        item = queue.pop(0)
         # i == current dict from list dict == data_json["packages"]
        for i in data_json["packages"]:
            #check if current dict has a key <item>
            if item == list(i.values())[0]: 
                #queue = list(i.values())[1]
                for j in list(i.values())[1]:
                    if j not in visited_from_bfs:
                        visited_from_bfs.append(j)
                        queue.append(j)
    return visited_from_bfs


visited_from_dfs = [] # declare empty list to store visited nodes


def dfs_search(visited, node): 
    """Function that keeps appending the visited nodes and their neighbours in DFS algorithm
    params : start_node: str
    return : all visited nodes with their dependancies: list
    """
    for i in data_json["packages"]:
            
            #checks if current dict has a key <item>
            if node == list(i.values())[0]:
                 # checks if the current node is unvisited - if yes, it is appended in the visited set.
                 if node not in visited_from_dfs:
                    visited_from_dfs.append(node)
                    #for each neighbor == list(i.values())[1] of the current node, the dfs function is invoked again
                    for j in list(i.values())[1]:
                        dfs_search(visited_from_dfs, j)

    return visited_from_dfs


if __name__ == "__main__":

    starting_node = "A"
    #print(f"Tree traversal using the \"BFS algorithm\": {bfs_search(starting_node)}")
    print(f"Tree traversal using the \"DFS algorithm\": {dfs_search([], starting_node)}")