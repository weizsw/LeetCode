class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        memoList = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j] and memoList[i]+1 > memoList[j]:
                    memoList[j] = memoList[i]+1

        return max(memoList)