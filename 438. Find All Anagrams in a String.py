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
                
        
        
        
