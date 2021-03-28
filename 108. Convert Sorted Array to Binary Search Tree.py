'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
'''


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(left, right):
            
            if left > right:
                return None
            
            p = (left + right)//2
            
            root = TreeNode(nums[p])
            
            root.left = helper(left, p-1)
            root.right = helper(p+1, right)
            
            return root
        
        
        return helper(0, len(nums)-1)
        
