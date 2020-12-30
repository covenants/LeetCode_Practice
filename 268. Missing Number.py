class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = -10
        
        for i in range(len(nums)):
            
            if i not in nums:
                n = i
        
        if n < 0:
            return len(nums)
        else:
            return n
