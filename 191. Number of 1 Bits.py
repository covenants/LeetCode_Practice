class Solution:
    def hammingWeight(self, n: int) -> int:
        
        result = str(bin(n)).count('1')
        
        return result
        
