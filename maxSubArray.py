class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = 0
        largest_sum = -float('inf')
   
        for n in nums:            
            if temp <= 0:
                temp = n
            else:
                temp +=n

            if temp > largest_sum:
                largest_sum = temp
        
        #print(largest_sum)
        
        return largest_sum
        
