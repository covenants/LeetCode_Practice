# Official solution

# My solution is below after this

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()
        
        output = []
        
        # sliding window on the string s
        for i in range(ns):
            
            # add one more letter 
            # on the right side of the window
            
            s_count[s[i]] += 1
            # remove one letter 
            # from the left side of the window
            
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
                    
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output
    
    
# My solution got TLE 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if s == p:
            return 0
        
        
        i = 0
        
        indexes = []
        
        b = sorted(p)
        
        while i < len(s) -len(p) +1:
            
            a = sorted(s[i:i + len(p)])
            
            if a == b:
                indexes.append(i)
            
            
            if len(set(a) & set(b)) == 0:
                i = i + len(p)
                continue
            
            i +=1
            
        
        #print(indexes)
        
        return indexes
                
        
        
        
