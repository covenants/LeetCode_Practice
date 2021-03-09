# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        
        queue = deque()
        result = []
        
        queue.append(root)
        
        while queue:
            
            level = len(queue)
            
            for i in range(level):
                
                node = queue.popleft()
                if i == level or i == level -1:
                    result.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
        
        print(result)
        
        return result
    
                
        
