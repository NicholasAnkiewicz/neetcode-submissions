# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if lists[0] == []:
            return None
        res = ListNode(0, None)
        head = res
        while len(lists) != 1:
            min_idx = min(range(len(lists)), key=lambda i: lists[i].val)
            smallest = lists[min_idx]
            print(lists[min_idx].val)
            head.next = smallest
            head = head.next 
            if lists[min_idx].next == None:
                lists.pop(min_idx)
            else:
                lists[min_idx] = smallest.next
        head.next = lists[0]
        return res.next