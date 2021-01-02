class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        
        permutations = collections.deque()
        permutations.append([])
        
        for num in nums:
            
            n = len(permutations)
            for _ in range(n):
                oldP = permutations.popleft()
                
                for j in range(len(oldP) +1):
                    newP = list(oldP)
                    newP.insert(j, num)
                    
                    if len(newP) == len(nums):
                        result.append(newP)
                    else:
                        permutations.append(newP)
        
        return result
