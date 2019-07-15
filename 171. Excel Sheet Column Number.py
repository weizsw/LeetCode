class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        l2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        alpha = dict(zip(l2,l1))
        value = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                value += alpha[s[i]]
            else:
                temp = 26 ** (len(s) - 1 - i) * alpha[s[i]]
                value += temp
        return value

