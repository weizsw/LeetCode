# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, cur_sum = de.pop()
            if not node.left and not node.right and cur_sum == 0:
                return True
            if node.right:
                de.append((node.right, cur_sum - node.right.val))
            if node.left:
                de.append((node.left, cur_sum - node.left.val))
        return False


