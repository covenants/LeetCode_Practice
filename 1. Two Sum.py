class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums = [2,7,11,15], target = 9
        #        [7, 2]
        
        if len(nums) == 0 or target is None:
            return []
        
        d = {}
        for index, num in enumerate(nums):
            
            if num not in d:
                d[target-num] = index
            else:
                return [index, d[num]]
