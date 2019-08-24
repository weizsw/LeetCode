class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        ans = 1
        while n :
            if n % 2:
                ans = x * ans
                n -= 1
            else:
                x = x * x
                n = n // 2
        return ans