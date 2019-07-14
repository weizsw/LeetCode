class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []
        nums.sort()

        length = len(nums) - 1
        # temp = []
        res = []
        # -4,-1,-1,0,1,2
        for i in range(length + 1):
            left = i
            right = length
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                while left < right:
                    if left == i:
                        left += 1
                    elif right == i:
                        right -= 1
                    elif nums[i] + nums[left] + nums[right] == 0:
                        # temp = [nums[i],nums[left],nums[right]]
                        res.append((nums[i],nums[left],nums[right]))
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -=1
                        right -= 1
                        continue
                    elif nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    else:
                        right -= 1
        return res

    # def threeSum(self, nums):
    # res = []
    # nums.sort()
    # for i in xrange(len(nums)-2):
    #     if i > 0 and nums[i] == nums[i-1]:
    #         continue
    #     l, r = i+1, len(nums)-1
    #     while l < r:
    #         s = nums[i] + nums[l] + nums[r]
    #         if s < 0:
    #             l +=1
    #         elif s > 0:
    #             r -= 1
    #         else:
    #             res.append((nums[i], nums[l], nums[r]))
    #             while l < r and nums[l] == nums[l+1]:
    #                 l += 1
    #             while l < r and nums[r] == nums[r-1]:
    #                 r -= 1
    #             l += 1; r -= 1
    # return res