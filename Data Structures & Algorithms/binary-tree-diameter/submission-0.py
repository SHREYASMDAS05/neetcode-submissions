# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0

        def solve(root):
            nonlocal d
            if root is None:
                return 0 

            left = solve(root.left)
            right = solve(root.right)
            d = max(d , left + right)
            return 1 + max(left , right)
        solve(root)
        return d
        
