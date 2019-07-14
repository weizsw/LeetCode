class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            return list(str(digits[0]+1))
        integer = 0
        length = len(digits)
        for i in range(length):
            integer += digits[i] * (10 ** (length - 1))
            length -= 1
        integer += 1
        return list(str(integer))
