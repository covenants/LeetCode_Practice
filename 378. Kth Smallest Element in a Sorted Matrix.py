
'''
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
'''


import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        l = []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                l.append(matrix[r][c])

        heapq.heapify(l)
        value = heapq.nsmallest(k, l)
        
        return value[-1]
            
