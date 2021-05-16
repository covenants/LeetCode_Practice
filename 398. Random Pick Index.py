'''
Given an integer array nums with possible duplicates, 
randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. 
If there are multiple valid i's, then each index should have an equal probability of returning.
 

Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

'''

import random

class Solution:

    def __init__(self, nums: List[int]):
        
        self.d = defaultdict(list)
        
        for index, n in enumerate(nums):
            self.d[n].append(index)
            
        

    def pick(self, target: int) -> int:
        
        matched_values = self.d[target]
        
        return random.choice(matched_values)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
