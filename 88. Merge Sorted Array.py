class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0 or len(nums2) == 0:
            pass
        else:
            
            for j in range(m, m+n):
                nums1[j] = nums2.pop(0)

            nums1.sort()
