
class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == None or root == p or root == q:
            return root
        
        # find p/q in left sub-tree
        l = self.lowestCommonAncestor(root.left, p, q)
        
        # find p/q in right sub-tree
        r = self.lowestCommonAncestor(root.right, p, q)
        
        # if p and q found in left or right subtree then its the lca
        if l and r:
            return root
        
        # else return the higher of the two nodes
        if l:
            return l
        else:
            return r
    







# Definition for a binary tree node.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p == root or q == root:
            return root

        if root is None:
            return None

        def lca(node):
            if not node:
                return False
            else:
                print(node.val)

            left = lca(node.left)
            right = lca(node.right)
            # If the current node itself is one of p or q,
            # we would mark a variable mid as True and continue the search
            # for the other node in the left and right branches.
            mid = node == p or node == q
            print('left ', left, ' right ', right, ' mid ', mid, ' node val ', node.val)

            # This counts the number of true statements (mid is true and then either left or right is true)
            # hence that will be the lca
            if mid + left + right >= 2:
                print(node.val)
                self.ans = node

            return mid or left or right

        lca(root)
        return self.ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)


a = Solution()
output = a.lowestCommonAncestor(root, root.left.left.right, root.left.right.right)
print(output.val)
