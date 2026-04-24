# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append([root, 0])
        res = []
        while q:
            cur = q.popleft()
            print(res)
            if len(res) < cur[1]+1:
                res.append([cur[0].val])
            else:
                res[cur[1]].append(cur[0].val)
            print(res)
            if cur[0].left:
                q.append([cur[0].left, cur[1]+1])
            if cur[0].right:
                q.append([cur[0].right, cur[1]+1])
        return res
