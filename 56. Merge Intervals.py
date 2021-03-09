class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        result = []
        result.append(intervals.pop(0))
        
        i = 0
        
        while i < len(intervals):
            
            if result[-1][1] >= intervals[i][0]:
                start, end = result.pop(-1)
                result.append([min(start, intervals[i][0]), max(end, intervals[i][1])])
                i +=1
                
            else:
                result.append(intervals[i])
                i +=1
                
        
        print(result)
        
        return result
        
