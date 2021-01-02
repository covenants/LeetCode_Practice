import heapq

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def traverse(root):
            
            nonlocal inorder
            
            if root:
                traverse(root.left)
                inorder.append(root.val)
                traverse(root.right)
        
        inorder = []
        
        traverse(root)
        heapq.heapify(inorder)
        smallest = heapq.nsmallest(k, inorder)[-1]
        
        print(smallest)
        
        return smallest
