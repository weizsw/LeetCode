class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for list in board:
#             print(list)
            nums = ["1","2","3","4","5","6","7","8","9"]
            for num in list:
                if num in nums:
                    nums.remove(num)
                elif num == '.':
                    continue
                else:
                    return False

        for i in range(0,9):
            nums = ["1","2","3","4","5","6","7","8","9"]
            for j in range(0,9):
                if board[j][i] in nums:
                    nums.remove(board[j][i])
                elif board[j][i] == ".":
                    continue
                else:
                    return False

        n = 0
        m = 3
        k = 0
        l = 3
        while (m <= 9):
            nums = ["1","2","3","4","5","6","7","8","9"]
            for i in range(n,m):
                for j in range(k,l):
                    if board[i][j] in nums:
                        nums.remove(board[i][j])
                    elif board[i][j] == '.':
                        continue
                    else:
                        return False
            k += 3
            l += 3
            if l > 9:
                k = 0
                l = 3
                n += 3
                m += 3

        return True






