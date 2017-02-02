# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [root]
        reserve = False
        while stack:
            if reserve:
                res.append([n.val for n in stack][-1::-1])
                reserve = False
            else:
                res.append([n.val for n in stack])
                reserve = True
            stack = [ i for k in stack for i in (k.left,k.right) if i ]
        return res
