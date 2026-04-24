# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Set a range while going down the tree. 
        #DFS while maintain range
        stack = [(root, [-math.inf, math.inf])]
        while stack:
            cur = stack.pop()
            if cur[0]:
                if cur[0].val >= cur[1][1] or cur[0].val <= cur[1][0]:
                    return False
                stack.append((cur[0].left, [cur[1][0], cur[0].val]))
                stack.append((cur[0].right, [cur[0].val, cur[1][1]]))
                #print(stack)
        return True