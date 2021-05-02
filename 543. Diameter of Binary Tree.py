
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diameter = 0
        #left_depth, right_depth = 0, 0
        
        def count_path(node):
            
            nonlocal diameter
            
            if not node:
                return 0
            
            left_depth = count_path(node.left)
            right_depth = count_path(node.right)
            
            diameter = max(diameter, left_depth + right_depth)
            
            return max(left_depth, right_depth) + 1
            
        
        count_path(root)

        return diameter
        
        
 '''
 Complexity Analysis

Let NN be the number of nodes in the tree.

Time complexity: O(N). This is because in our recursion function longestPath, 
we only enter and exit from each node once. We know this because each node is entered 
from its parent, and in a tree, nodes only have one parent.

Space complexity: O(N). The space complexity depends on the size of our implicit
call stack during our DFS, which relates to the height of the tree. In the worst case, 
the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(logN).
 '''
