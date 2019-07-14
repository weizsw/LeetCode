class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                return True
            else:
                index += 1
        return False