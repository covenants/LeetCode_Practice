class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        
        right = [0] * len(nums)
        left = [0] * len(nums)
        
        left[0] = 1
        right [len(nums)-1] = 1
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            
        for j in reversed(range(len(nums)-1)):
            right[j] = right[j+1] * nums[j+1]

        
        final = []
        
        for i in range(len(nums)):
            final.append(left[i] * right[i])
            
        #print(final)
        
        return final
