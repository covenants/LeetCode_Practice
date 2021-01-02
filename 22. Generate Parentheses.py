class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 0:
            return []
        
        
        def isvalid(A):
            
            counter = 0
            
            #print(A)
            for b in A:
                
                if b == '(':
                    counter +=1
                else:
                    counter -=1
                    
                if counter < 0:
                    return False
            
            return counter == 0
        
        
        def generate(n, A=[]):
            
            nonlocal result
            
            if len(A) == 2 * n:
                #print(A)
                if isvalid(A):
                    result.append(''.join(A))
            else:
                A.append('(')
                generate(n, A)
                A.pop()
                A.append(')')
                generate(n, A)
                A.pop()
        
        
        result = []
        generate(n)
        
        print(result)
        
        return result
