# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #clculte by height inside add condition if you got -1 from left or right return -1
        #if difference is greater than 1 return -1
        def solve(root):
            if root is None:
                return 0
            lt = solve(root.left)
            if lt == -1:
                return -1
            rt = solve(root.right)
            if rt == -1:
                return -1

            if abs(lt - rt) > 1:
                return -1 

            return 1 + max(lt , rt)

        x = solve(root)
        if x == -1:
            return False
        else:
            return True

        

        
        