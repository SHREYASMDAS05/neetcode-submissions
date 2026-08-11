# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
if root == None:
            return 0
        cnt = 0
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            cnt +=1

        return cnt
        '''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left , right)
        
        