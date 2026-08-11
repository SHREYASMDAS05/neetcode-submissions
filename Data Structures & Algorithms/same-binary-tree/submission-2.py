# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)

        while q1 and q2:
            e1 , e2 = q1.popleft() , q2.popleft()
            if e1.val != e2.val:
                return False

            if (e1.left is None) != (e2.left is None):
                return False
            if (e1.right is None) != (e2.right is None):
                return False
            if e1.left:
                q1.append(e1.left)
            if e1.right:
                q1.append(e1.right)
            if e2.left:
                q2.append(e2.left)
            if e2.right:
                q2.append(e2.right)

        return True
        '''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q :
                return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left , q.left) and
            self.isSameTree(p.right , q.right))

        return False

