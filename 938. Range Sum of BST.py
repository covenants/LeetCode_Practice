# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        def traverse(node, low, high):
            
            nonlocal total
            
            if node:
                if node.val <= high and node.val >= low:
                    total +=node.val
                if node.val >= low:
                    traverse(node.left, low, high)
                if node.val <= high:
                    traverse(node.right, low, high)
        
        total = 0
        traverse(root, low, high)
        
        print(total)
        
        return total
