class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = str(s).lstrip().rstrip()
        
        s = s.split()
        
        s = s[::-1]
        
        print(' '.join(s))
        
        return ' '.join(s)
