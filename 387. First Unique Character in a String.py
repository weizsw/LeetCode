class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
#         count = collections.Counter(s)

#         for index, ch in enumerate(s):
#             if count[ch] == 1:
#                 return index
#         return -1

        res = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            if i == s.rfind(c):
                return i
        return -1