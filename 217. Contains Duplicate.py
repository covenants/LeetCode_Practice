class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] == 2:
                return True
        
        return False
        
        
