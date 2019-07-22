class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        elif len(s) == 1:
            return 1
        else:
            temp = s[0]
            max_len = 1
            i = 0
            for letter in s[1:]:
                if letter in temp:
                    i = temp.find(letter)
                    temp = temp[i+1:]
                temp += letter
                if len(temp) > max_len:
                    max_len = len(temp)
            return max_len
#         used = {}
#         max_length = start = 0
#         for i, c in enumerate(s):
#             if c in used and start <= used[c]:
#                 start = used[c] + 1
#             else:
#                 max_length = max(max_length, i - start + 1)

#             used[c] = i


#         return max_length