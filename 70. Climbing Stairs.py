class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        d = [0] * (n+1)
        d[1] = 1
        d[2] = 2
        
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
            
        return d[n]
            
        
