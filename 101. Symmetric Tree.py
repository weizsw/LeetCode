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

        def isMirror(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            return (left.val == right.val and isMirror(left.right, right.left) and isMirror(left.left, right.right))
        return isMirror(root, root)
