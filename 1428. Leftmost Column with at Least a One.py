# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        
        dim = binaryMatrix.dimensions()
        rows, columns = dim
        
        # by default it is the last column
        min_index_values = columns
        
        for row in range(rows):
        
            l, h = 0, columns - 1

            while l < h:

                mid = l + (h -l) // 2

                if binaryMatrix.get(row, mid) == 0:
                    l = mid + 1
                else:
                    h = mid

            if binaryMatrix.get(row, l) == 1:
                # we store the column value and return the lowest column value
                # among all the rows
                min_index_values = min(min_index_values, l)
        
        # if it is not the last column, so we have a value less than max col value
        if min_index_values != columns:
            return min_index_values
                
        return -1
        
