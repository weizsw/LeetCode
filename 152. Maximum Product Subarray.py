class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max, _min, res = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            tmp = _min
            _min = min(num, min(_max*num, _min*num))
            _max = max(num, max(_max*num, tmp*num))
            res = max(res, _max)

        return res