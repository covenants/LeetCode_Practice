'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''

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
        
