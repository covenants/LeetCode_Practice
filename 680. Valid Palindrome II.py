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
