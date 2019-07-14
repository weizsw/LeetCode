class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        zero_list = []
        l = len(nums) - 1
        for i in range(l):
            if nums[i] == 0:
                count += 1
                zero_list.append(i)
        diff = 0
        for item in zero_list:
            nums.pop(item - diff)
            diff += 1
        for i in range(count):
            nums.append(0)

