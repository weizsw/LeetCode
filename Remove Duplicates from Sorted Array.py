class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_index = 0
        while current_index < len(nums) - 1:
            if nums[current_index] == nums[current_index + 1]:
                nums.pop(current_index)
                current_index -= 1
            current_index += 1
        return len(nums)

solution = Solution()
print(solution.removeDuplicates([1,1,1,1,2]))

