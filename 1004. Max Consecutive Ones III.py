# https://leetcode.com/problems/max-consecutive-ones-iii/

'''
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

'''
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        start, end, max_repeats = 0, 0, 0
        maxi = 0
        
        for end in range(len(A)):
            
            if A[end] == 1:
                max_repeats +=1
            
            if (end - start + 1 -max_repeats) > K:
                if A[start] == 1:
                    max_repeats -=1
                start +=1
                
            maxi = max(maxi, end-start+1)
            
        
        return maxi
                    
            

        
        