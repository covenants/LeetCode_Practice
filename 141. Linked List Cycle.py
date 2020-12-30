class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
