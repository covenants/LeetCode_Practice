class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        diff = 0
        max_diff = 0
        peak = -1
        
        if nums.index(max(nums)) == len(nums)-1:
            return nums.index(max(nums))
            
        for i in range(0, len(nums)-1):
            
            print(i, nums[i])
            # if the first element is peak
            if i == 0:
                if nums[i] > nums[i+1]:
                    peak = i
                    break
                    
            # any of the middle element is peak
            if i > 0:
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                    peak = i
                    break

            # if the last element is peak
            if i+1 == len(nums) -1:
                if nums[i+1] > nums[i]:
                    peak = i
                    break
            
            
        print(peak)
        
        if peak >=0:
            return peak
    
            
