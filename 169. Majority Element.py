class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # max_count = 1
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     try:
        #         if nums[i] == nums[i+1]:
        #             max_count += 1
        #             if max_count > len(nums)/2:
        #                 return nums[i]
        #         else:
        #             max_count = 1
        #     except IndexError:
        #         break
        nums.sort()
        return nums[len(nums)/2]

        # return sorted(nums)[len(nums)/2]