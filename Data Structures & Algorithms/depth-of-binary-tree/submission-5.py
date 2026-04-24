# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = deque()
        queue.append([root, 1])
        while queue:
            top = queue.popleft() 
            if top[0].left:
                queue.append([top[0].left, top[1]+1])
            if top[0].right:
                queue.append([top[0].right, top[1]+1])
        return top[1]
                    