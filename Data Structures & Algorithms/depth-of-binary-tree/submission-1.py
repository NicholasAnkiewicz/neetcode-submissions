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
        if root.left == None and root.right == None:
            return 1
        queue = []
        queue.append([root, 1])
        while len(queue) is not 0:
            top = queue.pop(0) 
            if top[0].left:
                queue.append([top[0].left, top[1]+1])
            if top[0].right:
                queue.append([top[0].right, top[1]+1])
        return top[1]
                    