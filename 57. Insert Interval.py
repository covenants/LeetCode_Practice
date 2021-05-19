'''
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])
        
        result = []
        
        result.append(intervals[0])
        intervals.pop(0)
        
        
        while intervals:
            
            rstart, rstop = result[-1]
            istart, istop = intervals.pop(0)
            
            if rstop >= istart:
                newstart, newstop = min(istart, rstart), max(istop, rstop)
                result.pop(-1)
                result.append([newstart, newstop])
            else:
                result.append([istart, istop])
            
        print(result)
        
        return result
            
            
