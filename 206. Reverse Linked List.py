# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        cur = head
        next_ = None
        prev = None
        
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
            
        return prev
