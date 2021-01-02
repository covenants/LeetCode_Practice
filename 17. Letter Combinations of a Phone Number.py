class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        numbers = {'1':[],
                  '2':['a','b','c'],
                  '3':['d','e','f'],
                  '4':['g', 'h', 'i'],
                  '5':['j','k','l'],
                  '6':['m','n','o'],
                  '7' : ['p','q','r','s'],
                  '8': ['t','u','v'],
                  '9': ['w','x','y','z'],
                  '0':[]}
        
        
        def backtrack(combinations, next_digits):
            
            if len(next_digits) == 0:
                output.append(combinations)
                
            else:
                
                for letter in numbers[next_digits[0]]:
                    backtrack(combinations+letter, next_digits[1:])
        
        
        output = []
        if digits:
            backtrack("", digits)
            
        return output
        
        
