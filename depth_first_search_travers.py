

visited = []

def depth_first_search(visited, dictionary, node): 
    if node not in visited:
        visited.append(node)
        for x in dictionary[node]:
            depth_first_search(visited, dictionary, x)
    return visited