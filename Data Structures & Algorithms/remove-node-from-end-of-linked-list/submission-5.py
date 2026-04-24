# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Use two pointers. 1 normal traverse = np, 1 n-1 nodes away from np
        np = head
        rp = head
        dist = 0
        while np.next:
            
            np = np.next
            if (n) == dist:
                rp = rp.next
            else:
                dist += 1
            print("np: " + str(np.val))
            print("rp: " + str(rp.val))
            print(dist)
        #print(prev.val)
        #print(rp.val)
        if dist == 0:
            return None
        if dist == 1:
            if n == 2:
                return np
            else:
                rp.next = None
                return head
        else:
            if dist != n:
                head = head.next
            rp.next = rp.next.next
        return head
        
        #print(rp.val)

