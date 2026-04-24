# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left != None:
            left = self.invertTree(root.left)
        else:
            left = None
        if root.right != None:
            right = self.invertTree(root.right)
        else:
            right = None
        root.left = right
        root.right = left
        return root
        