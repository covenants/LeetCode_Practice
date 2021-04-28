class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        # using Dynamic programming
        rows, cols = len(nums1), len(nums2)
        
        d = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        
        max_val = 0
        
        for i in range(rows):
            for j in range(cols):
                if nums1[i] == nums2[j]:
                    d[i][j] = d[i-1][j-1] + 1
                    max_val = max(max_val, d[i][j])
        
        
        return max_val
        
