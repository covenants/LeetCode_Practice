'''
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

'''


class Solution:
    
    def find_value(self, num):
        
        d ={}
        
        d[1] = 'One'
        d[2] = 'Two'
        d[3] = 'Three'
        d[4] = 'Four'
        d[5] = 'Five'
        d[6] = 'Six'
        d[7] = 'Seven'
        d[8] = 'Eight'
        d[9] = 'Nine'
        d[10] = 'Ten'
        d[11] = 'Eleven'
        d[12] = 'Twelve'
        d[13] = 'Thirteen'
        d[14] = 'Fourteen'
        d[15] = 'Fifteen'
        d[16] = 'Sixteen'
        d[17] = 'Seventeen'
        d[18] = 'Eighteen'
        d[19] = 'Nineteen'
        d[20] = 'Twenty'
        d[30] = 'Thirty'
        d[40] = 'Forty'
        d[50] = 'Fifty'
        d[60] = 'Sixty'
        d[70] = 'Seventy'
        d[80] = 'Eighty'
        d[90] = 'Ninety'
        d[100] = 'Hundred'
        
        res = []
        
        rem = num // 100
        if rem > 0:
            res.append(d[rem])
            res.append("Hundred")
            num = num % 100
        
        rem = num // 10
        # if the reminder is zero and the number not zero then it 
        # is between 1 and 9
        if rem == 0 and num!=0:
            res.append(d[num])
        
        elif rem == 1 and num!=0:
            res.append(d[num])
            
        elif rem > 0:
            res.append(d[rem * 10])
            num = num - (rem * 10)
            if num:
                res.append(d[num % 10])
                
        return res
        
    
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return "Zero"
        
        res = []
        
        rem = num // 10 ** 9
        if rem > 0:
            res += self.find_value(rem)
            res.append("Billion")
            num = num % (10 **9)
        
        rem = num // 10 ** 6
        if rem > 0:
            res += self.find_value(rem)
            res.append("Million")
            num = num % (10 **6)
            
        rem = num // 10 ** 3
        if rem > 0:
            res += self.find_value(rem)
            res.append("Thousand")
            num = num % (10 ** 3)
            
        rem = self.find_value(num)
        res +=(rem)
        
        return " ".join(res)
    
        
        
        
        
        
        
        
        
        
            
            
            
        
        
        
        
        
