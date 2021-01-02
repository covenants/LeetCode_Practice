
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        prev = None
        
        while root:
            if p.val < root.val:
                prev = root
                root = root.left
            else:
                root = root.right
                
        return prev
        
