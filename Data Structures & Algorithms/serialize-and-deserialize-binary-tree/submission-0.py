# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if not root:
            return "N,"
        q = deque([root])
        while q:
            cur = q.popleft()
            if not cur:
                res += ("N")
                res += (",")
            else:
                res += str(cur.val)
                res += (",")
                q.append(cur.left)
                q.append(cur.right)
        return res
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")[:-1]
        print(data)
        if data[0] == "N":
            return None
        root = TreeNode(data[0], None, None)
        q = deque([root])
        i = 1
        while q:
            cur = q.popleft()
            left = data[i]
            right = data[i+1]
            if left == "N":
                cur.left = None
            else:
                left_node = TreeNode(int(left), None, None)
                cur.left = left_node
                q.append(left_node)
            if right == "N":
                cur.right = None
            else:
                right_node = TreeNode(int(right), None, None)
                cur.right = right_node
                q.append(right_node)
            i += 2
        return root