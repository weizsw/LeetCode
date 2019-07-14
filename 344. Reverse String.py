class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)):
        #     s.insert(i,s[-1])
        #     s.pop()

        # s.reverse()

        left = 0
        right = len(s) -1
        temp = ''

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1


