class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if head is None:
            return head
        
        slow = head
        fast = head
        
        i = 0
        while i < n:
            fast = fast.next
            i +=1
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
            
        return head
