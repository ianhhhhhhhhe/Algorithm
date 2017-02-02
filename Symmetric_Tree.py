# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return isSym(l.left, r.right) and isSym(l.right, r.left)
            return False
        return isSym(root, root)
