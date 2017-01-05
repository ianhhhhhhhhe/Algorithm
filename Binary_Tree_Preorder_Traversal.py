# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        if root:
            stack.append(root.val)
            stack+=self.preorderTraversal(root.left)
            stack+=self.preorderTraversal(root.right)
        return stack
