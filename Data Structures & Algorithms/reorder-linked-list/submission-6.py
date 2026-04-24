# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Mid = right value when even
#Mid = mid value when odd
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Traverse with fast pointer moving 2 and slow moving 1
        #Get end and mid
        sp, fp = head, head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        #Reverse from mid to end
        re = sp.next
        prev = sp
        while re != None:
            temp = re.next
            re.next = prev
            prev = re
            re = temp
        sp.next = None
        l1 = head
        l2 = prev
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2
            
            