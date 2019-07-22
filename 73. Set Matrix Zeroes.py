class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        row = len(matrix)
        column = len(matrix[0])
#         row_index = set()
#         column_index = set()
#         for i in range(row):
#             for j in range(column):
#                 if matrix[i][j] == 0:
#                     row_index.add(i)
#                     column_index.add(j)

#         for i in range(row):
#             for j in range(column):
#                 if i in row_index or j in column_index:
#                     matrix[i][j] = 0
        first_row_has_zero = not all(matrix[0])
        for i in range(1, row):
            for j in range(column):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, row):
            for j in range(column -1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            matrix[0] = [0] * column
