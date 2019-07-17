class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def searchLow(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) / 2
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        def searchHigh(nums,target):
            low , high = 0 ,len(nums) - 1
            while low <= high:
                mid = (low + high) / 2
                if target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return high
        low, high = searchLow(nums, target), searchHigh(nums, target)
        return (low, high) if low <= high else [-1, -1]

