import math

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        result = []
        
        for p in points:
            result.append([math.sqrt(p[0]**2 + p[1]**2), p])
        
        result.sort(key=lambda x:x[0])
        r = []
        
        for i in range(K):
            r.append(result[i][1])
        
        return r
