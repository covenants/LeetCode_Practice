class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        d = {}
        
        i = 0
        while i < len(S):
            d[S[i]] = i
            i +=1

        j = 0
        anchor = 0
        
        result = []
        for i, c in enumerate(S):
            
            # find the max index for this character
            # next substring, d[c] will have higher value than j
            j = max(j, d[c])
            
            # if current index matches the max, index, then add it to anchor
            if i == j:
                result.append(i - anchor + 1)
                anchor = i + 1
                
        return result
        
        
