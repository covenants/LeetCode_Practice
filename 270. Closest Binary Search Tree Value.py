# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        
        def traverse(node, target):
            
            nonlocal cd
            nonlocal rval
            
            if node:
                
                if abs(node.val - target) < cd:
                    cd = abs(node.val - target)
                    rval = node.val
                if target > node.val:
                    traverse(node.right, target)    
                elif target < node.val:
                    traverse(node.left, target)
        
        cd = float('inf')
        rval = 0
        
        traverse(root, target)
        
        print(cd, rval)
        
        return rval
