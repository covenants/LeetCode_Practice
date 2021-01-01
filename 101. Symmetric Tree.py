class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        def traverse(root1, root2):
            
            if (root1 is None) and (root2 is None):
                return True
            
            if (root1 is None) or (root2 is None):
                return False
            
            return (root1.val==root2.val) and traverse(root1.left, root2.right) and traverse(root1.right, root2.left)
            
        
        result =  traverse(root, root)
            
        return result
