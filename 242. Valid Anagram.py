class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """

#         if len(s) != len(t):
#             return False
#         for letter in s:
#             if letter in t:
#                 t = t.replace(letter, '#', 1)
#                 continue
#             else:
#                 return False
#         return True

        def isAnagram(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            if len(s)==len(t):
                for char in set(s):
                    if s.count(char)!=t.count(char):
                        return False
                return True
            else:
                return False