class Solution:
    def trap(self, height: List[int]) -> int:
        
        i = 0
        j = 1
        water = 0
        
        size = len(height)
        
        if size < 1:
            return 0
        
        i, j = 0, 0
        
        left_max = [0] * size
        right_max = [0] * size
        
        # initialize left_max with left most element
        left_max[0] = height[0]
        
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i-1])
            
        # initialize right_max with right most element 
        right_max[size-1] = height[size-1]
        
        for i in range(size-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        # min of the two minus height of the bloack section
        # This adds water for index i only
        for i in range(1, size):
            water += min(right_max[i], left_max[i]) - height[i]
        
        return water
