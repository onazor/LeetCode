# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def traverse_tree(node: Optional[TreeNode], total):
            if not node:
                return 0
            total = 2*total+node.val
            if node.left == None and node.right == None:
                return total
            
            return traverse_tree(node.left, total) + traverse_tree(node.right, total)
        
        return traverse_tree(root, 0)
        