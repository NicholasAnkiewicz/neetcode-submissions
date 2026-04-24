# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #print("Preorder: " + str(preorder))
        #print("Inorder: " + str(inorder))
        if not preorder:
            return None
        root = preorder[0]
        mid = inorder.index(preorder[0])
        
        left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return TreeNode(root, left, right)