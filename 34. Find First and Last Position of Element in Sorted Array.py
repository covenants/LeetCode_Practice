class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]
        
        if target not in nums:
            return [-1, -1]
        
        range = []
        i = 0
        
        while i < len(nums):
            
            if nums[i] == target:
                range.append(i)
            
            i +=1
            
        if len(range) == 0:
            return [-1, -1]
        
        if len(range) == 1:
            return range * 2
        
        return  [range[0], range[-1]]
        
