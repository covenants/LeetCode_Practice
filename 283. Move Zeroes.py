class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # special cases
        ##############
        if sum(nums) == 0:
            return nums
        
        if len(nums) == 1:
            return nums
        
        if nums == sorted(nums, reverse=True):
            return 
        ###################
        
        i = 0
        j = 1
        
        ## 4 different possible combinations
        
        while j < len(nums):
            if nums[i] == 0 and nums[j] !=0:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
                j +=1
            elif nums[i] == 0 and nums[j] == 0:
                j +=1
            elif nums[i] !=0 and nums[j] != 0:
                j +=1
                i +=1
            elif nums[i] !=0 and nums[j] == 0:
                j +=1
                i +=1
        
