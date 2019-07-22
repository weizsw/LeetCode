class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        if not intervals:
            return []
        n = len(intervals)
        res = []
        start = end = intervals[0][0]

        i = 0
        while end < intervals[n-1][1]:
            if i < n and end >= intervals[i][0]:
                while i < n and end >= intervals[i][0]:
                    end = max(end, intervals[i][1])
                    i += 1
            else:
                res.append([start, end])
                start = end = intervals[i][0]
        res.append([start, end])
        return res