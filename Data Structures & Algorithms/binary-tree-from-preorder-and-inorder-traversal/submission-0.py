# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        print("Preorder: " + str(preorder))
        print("Inorder: " + str(inorder))
        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)
        root = preorder[0]
        mid = inorder.index(preorder[0])
        if mid != 0:
            left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        else:
            left = None
        if mid != len(inorder)-1:
            right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        else:
            right = None
        return TreeNode(root, left, right)