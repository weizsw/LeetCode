class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fact = 1

        # for i in range(1, n + 1):
        #     fact *= i
        # count = 0
        # mylist = []
        # for i in str(n):
        #     mylist.append(i)
        # for num in mylist[::-1]:
        #     if num == 0:
        #         count += 1
        #     else:
        #         break
        # return count
        r = 0
        while n > 0:
            n /= 5
            r += n
        return r