# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        res = []
        self.inorder(root, res)

        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False
        return True

    def inorder(self, root, res):

        if not root:
            return False

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)