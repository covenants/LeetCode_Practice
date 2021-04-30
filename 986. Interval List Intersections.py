class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        ans = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            
            # Intersection == max of start ... min of end 
            max_of_start = max(firstList[i][0], secondList[j][0])
            min_of_end = min(firstList[i][1], secondList[j][1])
            
            if max_of_start <= min_of_end:
                ans.append([max_of_start, min_of_end])
            
            # reject the smaller of the two list
            if firstList[i][1] < secondList[j][1]:
                i +=1
            else:
                j +=1
        
        #print(ans)
        
        return ans
