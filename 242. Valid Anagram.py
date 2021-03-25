'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # also can be done using Counter easily
        d1, d2 = {}, {}
        
        for i in s:
            d1[i] = d1.get(i, 0) + 1
        
        for j in t:
            d2[j] = d2.get(j, 0) + 1
        
        # Check if same number of characters
        if len(d1.keys()) != len(d2.keys()):
            return False
        
        for key, value in d1.items():
            if key in d1 and key in d2:
                if d1[key] != d2[key]:
                    return False
            else:
                return False
            
        return True
    
