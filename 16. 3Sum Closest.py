class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        res = sum(nums[:3])
        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s > target:
                    right -= 1
                else:
                    left += 1
        return res