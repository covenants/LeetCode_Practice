class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {')':'(', '}':'{', ']':'['}
        
        stack = []
        
        for b in s:
            if len(stack) > 0:
                if b in d:
                    if stack[-1] != d[b]:
                        return False
                    else:
                        stack.pop(-1)
                else:
                    stack.append(b)
            else:
                stack.append(b)
                
        if len(stack) == 0:
            return True
        
