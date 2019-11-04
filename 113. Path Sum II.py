# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        def dfs(path, left_sum, node):
            tmp = path[:]
            tmp.append(node.val)
            if not node.right and not node.left and left_sum == node.val:
                res.append(tmp)
            else:
                if node.right:
                    dfs(tmp, left_sum - node.val, node.right)
                if node.left:
                    dfs(tmp, left_sum - node.val, node.left)

        dfs([], sum, root)
        return res