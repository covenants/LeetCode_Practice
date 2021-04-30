class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # "(" that don't pair with a ")" are the ones we should remove. This way, we know we won't cause a negative balance.
        # So, remembering that each ")" was paired with the closest "(" that isn't already paired, 
        # how could we do this in code? We need to know the indexes of the problematic "("
        # 1. We can use a stack. Each time we see a "(", we should add its index to the stack. 
        # 2. If stack empty, we dont have an ( then for ) we need to remove it
        # 2. Each time we see a ")", we should remove an index from the stack because the ")" will match with whatever "(" was at the top of the stack. 
        # 3. Finally remove whatever is still in the stack and whatever is in the to_remove
        
        to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                to_remove.add(i)
            else:
                stack.pop()
        
        to_remove = to_remove.union(set(stack))
        string_builder = []
        
        for i, c in enumerate(s):
            if i not in to_remove:
                string_builder.append(c)
        
        return ''.join(string_builder)
