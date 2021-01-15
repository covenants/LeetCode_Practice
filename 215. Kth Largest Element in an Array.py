class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse=True)
        # heapq.nlargest(k, nums)[-1]
        
        return nums[k-1]
        
