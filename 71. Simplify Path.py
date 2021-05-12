class Solution:
    def simplifyPath(self, path: str) -> str:
        
        #s = str(path).strip()

        stack = []
        
        for c in path.split('/'):
            
            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if c == '..':
                if stack:
                    stack.pop()
            
            # A no-op for a "." or an empty string
            elif c == '.' or not c:
                continue
                
            else:
                stack.append(c)
                
        final = '/' + '/'.join(stack)
        
        return final
