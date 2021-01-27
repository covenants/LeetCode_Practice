class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        missing_numbers = []
        
        for i in range(1, max(arr) + k +1):
            if i not in arr:
                missing_numbers.append(i)
                if len(missing_numbers) == k:
                    print(missing_numbers)
                    return missing_numbers[k-1]
        
