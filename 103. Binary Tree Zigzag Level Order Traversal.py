from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        left_to_right = True
        res = []
        
        while queue:
            
            #stack = queue.leftpop()
            n_elements = len(queue)
            stack = deque()
            
            for i in range(n_elements):
                
                node = queue.popleft()
                #print(stack, queue)
            
                if left_to_right:
                    stack.append(node.val)
                else:
                    stack.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            
            res.append(list(stack))
            left_to_right = not left_to_right
            
        return res
                
