# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        self.list = []
        self.inorder(root)

        return self.list[k-1]

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.list.append(root.val)
        self.inorder(root.right)