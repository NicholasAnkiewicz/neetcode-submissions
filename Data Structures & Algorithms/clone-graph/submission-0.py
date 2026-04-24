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
        visted = {node: Node(node.val, [])}
        stack = []
        stack.append(node)
        while stack:
            cur = stack.pop()
            for v in cur.neighbors:
                print(v)
                print(v.val)
                if not visted.get(v):
                    visted[v] = Node(v.val, [])
                    stack.append(v)
                visted[cur].neighbors.append(visted[v])
        
        return visted[node]
