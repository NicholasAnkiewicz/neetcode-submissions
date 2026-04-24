# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        temp = None
        while cur != None:
            next_node = cur.next #1
            cur.next = temp
            temp = cur #
            cur = next_node
            
        head = temp
        return head

