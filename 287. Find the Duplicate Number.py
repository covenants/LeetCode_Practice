class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        d = {}
        
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > 1:
                return n
        
        
