class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        print(matrix)
        print(len(matrix[0]))
        
        for i in range(0, len(matrix[0])):
            for j in range(i, len(matrix[0])):
                if j != i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
       
        
        for i in range(len(matrix[0])):
            matrix[i].reverse()
