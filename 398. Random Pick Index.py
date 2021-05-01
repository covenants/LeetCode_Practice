import random

class Solution:

    def __init__(self, nums: List[int]):
        
        self.d = defaultdict(list)
        
        for index, n in enumerate(nums):
            self.d[n].append(index)
            
        

    def pick(self, target: int) -> int:
        
        matched_values = self.d[target]
        
        return random.choice(matched_values)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
