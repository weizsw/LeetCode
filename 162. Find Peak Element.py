class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        else:
            nums.insert(0, 0)
            nums.append(0)
            for i in range(1, len(nums) - 1):

                if nums[i] > nums[i-1] and nums[i] > nums[i + 1]:
                    return i - 1
        return 0