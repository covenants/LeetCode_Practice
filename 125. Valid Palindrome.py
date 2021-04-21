class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == reversed(s):
            return True
        
        if len(s) == 1:
            return True
        
        left = 0
        right = len(s) - 1
        
        while left <= right:
            
            while not s[left].isalnum():
                left +=1
                
                # extra check to see if it has no alphanumeric ',.'
                if left >= len(s):
                    return True
                
            while not s[right].isalnum():
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right -=1
            
            
        return True
        
        
        
##########################################################        




class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        
        s_new = []
        for s_ in s:
            if s_.isalnum():
                s_new.append(s_)
                
        s = ("").join(s_new)
        
        #print(s)
        
        if len(s) <= 1:
            return True
        
        i, j = 0, len(s)- 1
        
        while i < j:
            if not s[i].isalnum():
                i +=1
            if not s[j].isalnum():
                j -=1
            
            if s[i].lower() == s[j].lower():
                i +=1
                j -=1
            
            #print(i, j, s[i], s[j])
                
            #if s[i].isalpha() and s[j].isalpha() and s[i].lower() != s[j].lower():
            if s[i].lower() != s[j].lower():
                #print('This got executed')
                return False
            
            if i > j:
                return True
            
            
            if i ==j:
                return True
            
        return True
            
        
