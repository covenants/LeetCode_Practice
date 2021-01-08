class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = [[1]]
        
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        i = 0
        rows = 0
        
        last_row = result
        while rows !=numRows:
            new_row = (len(last_row) + 1) * [1]
            if rows ==1:
                rows +=1
                continue
            else:
                for i in range(1, len(last_row)):
                    new_row[i] = last_row[i-1] + last_row[i]
            rows +=1
            
            last_row = new_row
            result.append(new_row)
            
        print(result)
        
        return result
                    
