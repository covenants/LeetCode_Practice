class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        if n == 0:
            return []
        
        ans = []
        
        i = 0
        j = n
        
        while j  <= len(nums)-1:
            ans.append(nums[i])
            ans.append(nums[j])
            i = i + 1
            j = j + 1
            #print(i, j)
            
        print(ans)
        
        return ans
            
