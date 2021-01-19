'''
Not optimal
'''

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        a = []
        
        while head is not None:
            a.append(head.val)
            head = head.next
            
        if a == a[::-1]:
            return True
        
        return False
        
