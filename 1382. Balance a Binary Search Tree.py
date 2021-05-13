class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        balanced = []
        
        def traverse(node):
            
            if node:
                traverse(node.left)
                balanced.append(node.val)
                traverse(node.right)
                
        traverse(root)
        
        
        def bt(array):
            
            if not array:
                return
            
            mid = len(array) // 2
            node = TreeNode(array[mid])
            node.left = bt(array[:mid])
            node.right = bt(array[mid+1:])
                
            return node
        
        return bt(balanced)
