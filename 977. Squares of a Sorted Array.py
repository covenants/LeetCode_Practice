class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        sorted_array = [0] * n
        
        left, right = 0, len(nums)-1
        
        for i in range(n-1, -1, -1):
            
            if abs(nums[left]) < abs(nums[right]):
                sorted_array[i] =  nums[right] * nums[right]
                right -=1
            else:
                sorted_array[i] =  nums[left] * nums[left]
                left +=1
                

        print(sorted_array)
        
        return sorted_array
    
        
