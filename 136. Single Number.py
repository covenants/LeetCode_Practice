'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            nums[0]
        
        output = 0
        
        for X in nums:
            output = X ^ output
            
        print(output)
        
        return output
