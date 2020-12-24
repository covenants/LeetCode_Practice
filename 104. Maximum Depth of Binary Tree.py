# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        max_depth = 0
        
        def helper(node: TreeNode, depth):
            
            if node is None:
                return depth
            
            if root.left is None and root.right is None:
                return depth
        
            return max(helper(node.left, depth+1), helper(node.right, depth+1))
        
        
        result = helper(root, 0)
        
        print(result)
        
        return result
