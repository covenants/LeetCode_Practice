'''
https://leetcode.com/problems/regular-expression-matching/
'''

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if p == '.*':
            return True
        
        x = re.search(p, s)
        
        if x:
            if len(x.group(0)) == len(s):
                return True
        
        return False
    
           
        
        
