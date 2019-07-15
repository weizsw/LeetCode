class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        mylist = []
        for num in str(x):
            mylist.append(num)
        y = 0
        if mylist[0] != '-':
            mylist = mylist[::-1]
            leng = len(mylist) - 1
            for num in mylist:
                y += int(num) * 10 ** leng
                leng -= 1
        else:
            mylist.pop(0)
            mylist = mylist[::-1]
            leng = len(mylist) - 1
            for num in mylist:
                y += int(num) * 10 ** leng
                leng -= 1
            y = -y
        if abs(y) >= 2147483647:
            return 0
        return y