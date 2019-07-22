class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        while matrix:
            res += matrix[0]
            del(matrix[0])
            try:
                for list in matrix:
                    res.append(list.pop())
            except IndexError:
                break
            try:
                res += matrix[len(matrix) - 1][::-1]
                del(matrix[len(matrix) - 1])
                rev = []
                for list in matrix:
                    rev.append(list.pop(0))
                res += rev[::-1]
            except IndexError:
                break

        return res