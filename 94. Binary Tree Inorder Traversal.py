'''
Recursive
'''

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def inorder(node):
            
            nonlocal inorder_values
            
            if node:
                inorder(node.left)
                inorder_values.append(node.val)
                inorder(node.right)
            
        inorder_values = []
        inorder(root)
        
        return inorder_values
        
