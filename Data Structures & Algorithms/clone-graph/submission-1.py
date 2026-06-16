"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #old to new  pointer to old
        old_to_new = {}
        #iterate through our graph dfs 
        #build our graph as we hit each node
        visited = set()
        stack = [node]
        while stack:
            root = stack.pop()
            visited.add(root)
            old_to_new[root]= Node(root.val)
            for nei in root.neighbors:
                if nei in visited:continue
                stack.append(nei)
        #build our new graph
        for old,new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])
        return old_to_new[node]

        #build the edges between the node