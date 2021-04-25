class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.traversal = []
        
        def traverse(node):
            if node:
                traverse(node.left)
                self.traversal.append(node.val)
                traverse(node.right)
        
        traverse(root)
        
        #print('printing traversal ', self.traversal)
        #print('total nodes in the tree ', len(self.traversal))
        
        self.index = 0
        

    def next(self) -> int:
        
        temp = self.index
        
        self.index +=1
        
        return self.traversal[temp]

    def hasNext(self) -> bool:
        
        if self.index < len(self.traversal):
            return True
        else:
            return False
