'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True

Explanation: You could delete the character 'c'.
'''

### BruteForce
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True
        
        if s == s[::-1]:
            return True
        
        seen_so_far = []
        
        for i in range(len(s)):
            ss = s[:i] + s[i+1:]
            if ss == ss[::-1]:
                print(ss)
                return True
        
        return False

    
    
    #### Another approach (not brute force)
    class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if len(s) == 0: 
            return False
        
        if len(s) == 1:
            return True
        
        if s == s[::-1]:
            return True
        
        low = 0
        high = len(s) -1
        
        def cp(s, low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low +=1
                high -=1
            
            return True
        
        
        while low < high:
            
            if s[low] == s[high]:
                low +=1
                high -=1
                
            else:
                # check if removing 1 character makes it palindrom
                # if s[low+1..high] or s[low..high-1] is palindrom
                if cp(s, low+1, high) or cp(s, low, high-1):
                    return True
                else:
                    # else not palindrom
                    return False
        
        # by default palindrom
        return True
                
