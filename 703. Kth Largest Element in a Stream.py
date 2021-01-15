class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.nums = nums
        #self.sorted_nums = nums.sort(reverse=True)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        #print(self.nums)
        return self.nums[self.k-1]
