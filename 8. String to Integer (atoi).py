class Solution:
    def myAtoi(self, s: str) -> int:
        
        # remove whitespaces from before and after
        s = str(s).strip()
        
        # do all the checks for invalid string
        # 1. if length is zero, return 0
        if len(s) == 0:
            return 0
        
        # 2. length greater than 0 but the first character is neither sign not digit, return 0
        if len(s) > 0 and not(s[0] in ['+', '-'] or s[0].isdigit()):
            return 0
        
        sign = 1
        
        result = 0
        
        i = 0
        
        # 3. change sign
        if s[0] == '-':
            sign = -1
        
        # 4. increase index in case first index is sign
        if not s[0].isdigit():
            i = 1
        
        # 5. multiply previous value with 0 and add values
        while i < len(s) and s[i].isdigit():
            result = (result * 10) + (ord(s[i]) - ord('0'))
            i +=1
        
        # 6. multiply with sign
        result *= sign
        
        # 7. keep number within constrain
        if result > (2 ** 31) -1:
            result = (2 ** 31) -1
        elif result < -(2 ** 31):
            result = -(2 ** 31)
            
        
        print('final result ', result)
        
        return result
        
