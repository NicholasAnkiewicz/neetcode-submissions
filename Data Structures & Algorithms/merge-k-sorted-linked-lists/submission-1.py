# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        res = None
        smallest = None
        while len(lists) != 0:
            for i in range(len(lists)):
                if smallest == None or lists[i].val < lists[smallest].val:
                    smallest = i
            print(smallest)
            print(res)
            if res == None:
                res = lists[smallest]
                head = res
            else:
                res.next = lists[smallest]
                res = res.next

            if lists[smallest].next == None:
                lists.pop(smallest)
            else:
                lists[smallest] = lists[smallest].next
            smallest = None
        return head
        
        