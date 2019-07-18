class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        before_3_step = 0
        before_2_step = 0
        adj = 0
        for num in nums:
            before_3_step, before_2_step, adj = before_2_step, adj, max(before_3_step + num, before_2_step + num)
        return max(before_2_step, adj)

        #compare 2 and 3 steps + current num, store in 1 step before current num