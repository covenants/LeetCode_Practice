class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            n *= -1
            x  = 1/x
        elif n == 0:
            return 1
        
        power = 1
        current_result = x
        
        while n >0:
            
            if n % 2:
                power = power * current_result
            current_result = current_result * current_result
            n = n //2
        
        return power
        
