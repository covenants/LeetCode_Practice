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
