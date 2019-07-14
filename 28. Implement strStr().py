class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

#         for i in range(0, len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i

#         return -1