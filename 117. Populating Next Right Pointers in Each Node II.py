
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        
        if not root:
            return None
        
        if root.left is None and root.right is None:
            return root
        
        
        queue = collections.deque()
        
        n_levels = 0
        values_in_level = []
        
        queue.append(root)
        
        while queue:
            
            print('length of dequeue is ', len(queue))
            
            n_levels = len(queue)
            print('n levels', n_levels, len(queue))
            values_in_level = []
            
            prevNode = None
            
            for _ in range(n_levels):
                
                node = queue.popleft()
                values_in_level.append(node)
                
                # Simple logic to put prev node next pointer to current node
                if prevNode:
                    prevNode.next = node
                
                # prevNode pointer move to current node
                prevNode = node
                
                if node.left:
                    queue.append(node.left)
                    #values_in_level.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    #values_in_level.append(node.right)
            
        return root
                
                
                    
            
            
