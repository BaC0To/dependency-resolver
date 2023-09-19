# dependency-resolver
A program that reads a .json file containing three of dependancies (tree or graph)
later implementing the BFS and DFS algorithms to traverse (visit each node) a tree

Breadth-first search vs. depth-first search
A breadth-first search is when you inspect every node on a level starting at the top of the tree and then move to the next level. A depth-first search is where you search deep into a branch and don’t move to the next one until you’ve reached the end.

Depth-first search is not considered a complete algorithm since searching an infinite branch in a tree can go on forever. In this situation, an entire section of the tree would be left un-inspected.