class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for index in range(len(s)):
            temp = self.helper(s, index, index)
            if len(temp) > len(res):
                res = temp
            temp = self.helper(s, index, index+1)
            if len(temp) > len(res):
                res = temp
        return res



    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]