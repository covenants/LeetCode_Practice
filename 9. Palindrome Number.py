class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if len(str(x)) == 0:
            return False
        
        if len(str(x)) == 1:
            return True
        
        str_x = list(str(x))
        
        i, j = 0, len(str_x)-1
        
        while i <= j:
            if str_x[i] == str_x[j]:
                i +=1
                j -=1
                if i ==j:
                    return True
            else:
                return False
        
        print(i, j)
        # If they are same or i has gone past j 
        if abs(i-j)==1:
            return True
        else:
            return False
        
        
