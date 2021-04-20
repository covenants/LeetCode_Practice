'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true
'''

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        increasing = False
        decreasing = False
        
        i = 0
        
        while i < len(A)-1:
            
            if A[i] < A[i+1]:
                increasing = True
                
            elif A[i] > A[i+1]:
                decreasing = True
                
            if increasing == True and A[i] > A[i+1]:
                return False
            
            if decreasing == True and A[i] < A[i+1]:
                return False
            
            i +=1
            
        return True
