class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        
        if len(nums) == 2:
            return [0, 1]
        
        store = {}
        
        for index, n in enumerate(nums):
            
            if n in store.keys():
                return [index, store[n]]
            else:
                store[target - n] = index
            
