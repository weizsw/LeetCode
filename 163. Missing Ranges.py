class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums.insert(0, lower-1)
        nums.append(upper+1)
        for i in range(0, len(nums)-1):
            a = nums[i]
            b = nums[i+1]
            if a == b or a+1 == b:
                pass
            elif a+2 == b:
                res.append(str(a+1))
            else:
                res.append(str(a+1) + '->' + str(b-1))
        return res