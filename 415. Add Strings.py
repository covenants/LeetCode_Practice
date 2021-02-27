class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        integer = {'0':0,
                  '1':1,
                  '2':2,
                  '3':3,
                  '4':4,
                  '5':5,
                  '6':6,
                  '7':7,
                  '8':8,
                  '9':9}
        
        
        val1 = list(num1)[::-1]
        val2 = list(num2)[::-1]
        
        carry = 0
        result = []
        
        for i in range(max(len(val1), len(val2))):
            
            if i < len(val1) and i < len(val2):
                temp = integer[val1[i]] + integer[val2[i]]    
                temp += carry
                if temp < 10:
                    result.append(temp)
                    carry = 0
                else:
                    result.append(temp%10)
                    carry = 1
            elif i < len(val1):
                temp = integer[val1[i]]
                temp += carry
                result.append(temp)
                carry =0
            elif i < len(val2):
                temp = integer[val2[i]]
                temp += carry
                result.append(temp)
                carry = 0
                
        if carry == 1:
            result.append(1)
            
        result = result[::-1]
        
        value = 0
        
        for num in result:
            value = value * 10 + num
        
        print(str(value))
        
        return str(value)
                
        
        
