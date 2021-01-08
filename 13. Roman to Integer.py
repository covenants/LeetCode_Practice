class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbols = collections.defaultdict(list)
        # We put value and order in a dictionary
        symbols['I'].append([1,1])
        symbols['V'].append([5,2])
        symbols['X'].append([10,3])
        symbols['L'].append([50,4])
        symbols['C'].append([100,5])
        symbols['D'].append([500,6])
        symbols['M'].append([1000,7])
        

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return symbols[s][0][0]
        
        total = 0
        i = 0
        
        while i != len(s)-1:
            if symbols[s[i]][0][1] >= symbols[s[i+1]][0][1]:
                total += symbols[s[i]][0][0]
            else:
                total -= symbols[s[i]][0][0]
            i +=1
            #print(i, total)
            
        total += symbols[s[i]][0][0]

        return total
        
