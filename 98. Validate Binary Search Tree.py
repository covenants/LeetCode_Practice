import math

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        def validate(node, lower=-math.inf, higher=math.inf):
            
            if not node:
                return True
            
            if (node.val <= lower) or (node.val >= higher):
                return False
            
            return (validate(node.left, lower, node.val) and validate(node.right, node.val, higher))
            
        
        
        return validate(root, -math.inf, math.inf)
