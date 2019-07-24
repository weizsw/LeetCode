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
        res = []
        self.helper(res, 0, root)
        return res

    def helper(self, res, level, root):

        if not root:
            return
        elif len(res) <= level:
            res.append([root.val])
        elif not level%2:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)
        self.helper(res, level+1, root.left)
        self.helper(res, level+1, root.right)