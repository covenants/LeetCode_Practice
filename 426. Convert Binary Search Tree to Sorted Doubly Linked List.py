"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        def helper(node):
            
            nonlocal first, last
            
            if node:
                # keep going left
                helper(node.left)
            
                # linking with previous node, if exists
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node

                last = node

                # now go right
                helper(node.right)
        
        if not root:
            return None
        
        first, last = None, None
        helper(root)
        
        last.right = first
        first.left = last
        
        return first
        
        
