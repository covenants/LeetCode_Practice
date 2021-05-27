class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        # Return how many numbers are missing until nums[idx]
        # for 4, missing numbers are 1,2,3 total 3
        def missing(idx):
            return (nums[idx] - nums[0] + 1) - (idx + 1)
        
        n = len(nums)
        
        # if the kth missing number is larger than 
        # the last element of the array
        if k > missing(n-1):
            return nums[-1] + k - missing(n-1)
        
        
        left, right = 0, n-1
        # find left = right index such that 
        # missing(left - 1) < k <= missing(left)
        
        while left != right:
            pivot = left + (right-left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot
        
        # kth missing number is greater than nums[left - 1]
        # and less than nums[left]
        return nums[left -1] + k - missing(left-1)
        
        
        
        