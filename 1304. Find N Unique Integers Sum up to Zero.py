class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n == 1:
            return [0]
        
        if n ==2:
            return [-1, 1]
        
        result = []
        
        positive = 0
        negative = 0
        
        while n!=0:
            
            if n % 2==0:
                
                positive +=1
                result.append(positive)
            else:
                negative -=1
                result.append(negative)
                
            n -=1
        
        if sum(result) ==0:
            return result
        else:
            
            last_val = -sum(result[0:n])
            if last_val not in result:
                result.pop(-1)
                result.append(last_val)
                return result
        
