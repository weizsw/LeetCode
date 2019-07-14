class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        i = 0
        if nums[i] != nums[i+1]:
            return nums[i]
        elif nums[len(nums) - 2] != nums[len(nums) - 1]:
            return nums[len(nums) - 1]
        else:
            while i <= len(nums) - 1:
                    if nums[i] == nums[i+1]:
                        i += 2
                    else:
                        return nums[i]

