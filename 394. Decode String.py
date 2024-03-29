class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur_num = 0
        cur_str = ''
        stack = []

        for char in s:
            if char == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif char == ']':
                pre_num = stack.pop()
                pre_str = stack.pop()
                cur_str = pre_str + pre_num * cur_str
            elif char.isdigit():
                cur_num = cur_num * 10 + int(char)
            else:
                cur_str += char

        return cur_str
