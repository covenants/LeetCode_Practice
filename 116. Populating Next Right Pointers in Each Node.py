from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None:
            return
        
        queue = deque()
        queue.append(root)
        
        while queue:
            
            n_level = len(queue)
            prev_node = None
            print(n_level)
            
            for i in range(n_level):
                
                current_node = queue.popleft()
                
                if prev_node:
                    prev_node.next = current_node
                prev_node = current_node
                    
                if current_node.left:
                    queue.append(current_node.left)
                    
                if current_node.right:
                    queue.append(current_node.right)
                
        return root
