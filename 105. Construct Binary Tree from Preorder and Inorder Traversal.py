class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        def build_tree(preorder, inorder):
            
            if inorder:
                
                node_index = inorder.index(preorder.pop(0))
                node = TreeNode(inorder[node_index])
                node.left = build_tree(preorder, inorder[:node_index])
                node.right = build_tree(preorder, inorder[node_index+1:])

                return node

            
        
        root = preorder[0]
        node_index = inorder.index(root)
        print(node_index)
        root = TreeNode(root)
        
        return build_tree(preorder, inorder)
        
