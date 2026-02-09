# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals_list = []
        # define a function that sorts the root
        def depth_first_search(node):
            if node is None:
                return
            depth_first_search(node.left)
            vals_list.append(node.val)
            depth_first_search(node.right)

        depth_first_search(root)
        print(vals_list)
        # we write a recursive function that builds a balanced BST from vals_list
        
        def build(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            node = TreeNode(vals_list[middle])
            node.left = build(left, middle-1)
            node.right = build(middle+1, right)
            return node
        
        return build(0, len(vals_list)-1)