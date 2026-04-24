# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #If the root is between the two nodes (in value) then it is a ancestor
        #If both are greater than root then we go down right
        #If both are less than root then we go down left

        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        if p.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

