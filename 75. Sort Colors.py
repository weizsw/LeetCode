class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = one = two = 0
        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            elif num == 2:
                two += 2

        for i in range(len(nums)):
            if zero != 0:
                nums[i] = 0
                zero -= 1
            elif one != 0:
                nums[i] = 1
                one -= 1
            elif two != 0:
                nums[i] = 2
                two -= 1

#         def sortColors(self, nums):
#             red, white, blue = 0, 0, len(nums)-1

#             while white <= blue:
#                 if nums[white] == 0:
#                     nums[red], nums[white] = nums[white], nums[red]
#                     white += 1
#                     red += 1
#                 elif nums[white] == 1:
#                     white += 1
#                 else:
#                     nums[white], nums[blue] = nums[blue], nums[white]
#                     blue -= 1
