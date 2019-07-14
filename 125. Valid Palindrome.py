class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if not s:
        #     return True

        s = "".join(c for c in s if c.isalnum()).lower()

        f = s[::-1]

        if s == f:
            return True
        else:
            return False

        # l, r = 0, len(s)-1
        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while l <r and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l +=1; r -= 1
        # return True