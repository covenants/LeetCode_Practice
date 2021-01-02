class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        subsets.append([])
        
        for num in nums:
            
            n = len(subsets)
            
            for i in range(n):
                set = list(subsets[i])
                set.append(num)
                subsets.append(set)
        
        return subsets
        
        # set-> subset | set | subset-> set
        
        
