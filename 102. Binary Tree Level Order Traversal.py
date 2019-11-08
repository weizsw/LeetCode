# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        def helper(root, levels):

            if len(res) == levels:
                res.append([])

            res[levels].append(root.val)

            if root.left:
                helper(root.left, levels + 1)
            if root.right:
                helper(root.right, levels + 1)
        helper(root, 0)
        return res