class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])


        dp = [[0]*col for _ in range(row)]


        for i in range(col):
            dp[0][i] = 1 if matrix[0][i] == '1' else 0

        for i in range(row):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0

#         dp.append([0]*col)
#         for list in dp:
#             list.append(0)

        max_len = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    max_len = max(max_len, dp[i][j])

        return max(map(max, dp)) ** 2