class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # j = -1
        # for row in matrix:
        #     while j + len(row) >= 0 and row[j] > target:
        #         j -= 1
        #     if j + len(row) >= 0 and row[j] == target:
        #         return True
        # return False

        for row in matrix:
            if self.bs(row, target):
                return True
        return False

    def bs(self, matrix, target):
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high)/2

            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False