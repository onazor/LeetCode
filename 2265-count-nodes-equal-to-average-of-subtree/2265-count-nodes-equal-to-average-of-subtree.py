# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        counter = 0
        def helper_dfs(node):
            nonlocal counter
            if node is None:
                return (0,0)
            
            left_sum, left_count = helper_dfs(node.left)
            right_sum, right_count = helper_dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                counter += 1
            
            return (total_sum, total_count)
        
        helper_dfs(root)
        return counter

