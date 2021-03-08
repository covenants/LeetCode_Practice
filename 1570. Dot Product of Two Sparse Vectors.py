class SparseVector:
    
    def __init__(self, nums: List[int]):
        
        self.nums = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        total = 0
        print(self.nums)
        print(vec.nums)
        
        for i in range(len(self.nums)):
            total += self.nums[i] * vec.nums[i]
        
        return total
        


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n              

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result
 
