class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # 1. empty list
        if len(nums) == 0:
            return 1
        
        # list has one element but value less than or equal tto zero
        if len(nums) == 1:
            if nums[0] <= 0:
                return 1
        
        # find max_value
        max_value = max(nums)
        
        # max value less than 0
        if max_value < 0:
            return 1
        
        # lop through all values till max_value+2, return missing number
        for i in range(1, max_value+2):
            if i not in nums:
                print(i)
                return i
        
