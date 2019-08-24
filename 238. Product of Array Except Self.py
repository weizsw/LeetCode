class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [0] * length
        l = [0] * length
        r = [0] * length
        l[0] = 1
        for i in range(1, length):
            l[i] = l[i - 1] * nums[i - 1]

        r[length - 1] = 1
        for i in reversed(range(length - 1)):
            r[i] = r[i + 1] * nums[i + 1]

        for i in range(length):
            res[i] = l[i] * r[i]

        return res