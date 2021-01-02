'''
Iterative
'''

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def traverse(n):
            
            nonlocal stack
            nonlocal res
            
            while n!=None or len(stack)!=0:
                
                while n!=None:
                    stack.append(n)
                    n = n.left
                    
                n = stack.pop()
                res.append(n.val)
                n = n.right
            
            return res
        
        stack, res = [], []
        res = traverse(root)
        
        return res



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
        
