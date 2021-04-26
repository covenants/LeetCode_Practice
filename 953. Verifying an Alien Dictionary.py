class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d = {}
        
        for index, c in enumerate(list(order)):
            d[c] = index
            
        result = []
        
        left = 0
        right = 1
        diff = 0
        
        for i in range(len(words)-1):
            
            for j in range(len(words[i])):
                
                #  the former word is shorter, then words is sorted. However, 
                # if the latter word is shorter, then words is not sorted.
                if j >= len(words[i+1]):
                    return False
                
                # if not the same character, check if order is correct
                # we only check for first letter if order ok, then break (no need to check rest)
                if words[i][j] != words[i+1][j]:
                    if d[words[i][j]] > d[words[i+1][j]]:
                        return False
                    break
                    
                    
        return True
    
