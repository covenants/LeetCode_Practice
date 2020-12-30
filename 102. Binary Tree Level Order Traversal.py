from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            
            n_levels = len(queue)
            levels = []
            
            for i in range(n_levels):
                
                node = queue.popleft()
                levels.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(levels)
        
        print(result)
        
        return result
