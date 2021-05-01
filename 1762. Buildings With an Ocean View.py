class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        if len(heights) == 1:
            return [0]
        
        if len(heights) == 0:
            return [0]
        
        ans = []
        max_seen = 0
        # 1. start from end
        # 2. keep track of max height building
        # 3. if current height is higher than max height then current index can see
        # 4. update max height
        # 5. decrease i
        
        max_height = heights[-1]
        
        for i in range(len(heights)-1, -1, -1):
            if not max_seen or heights[i] > max_seen:
                ans.append(i)
                
                max_seen = max(heights[i], max_seen)
            
        
        print(ans)
        
        return ans[::-1]
