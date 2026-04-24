# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        head = res = ListNode()
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
                res = res.next
            else:
                res.next = l2
                l2 = l2.next
                res = res.next
        res.next = l1 or l2
        return head.next