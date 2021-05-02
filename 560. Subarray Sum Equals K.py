class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        
        for i in range(0, len(nums)):
            cumsum = 0
            for j in range(i, len(nums)):
                cumsum += nums[j]
                if cumsum == k:
                    ans +=1
        
        print(ans)
        
        return ans
            
