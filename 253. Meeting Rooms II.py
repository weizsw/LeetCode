class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort()

        free_rooms = []

        heapq.heappush(free_rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if  free_rooms[0] <= intervals[i][0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, intervals[i][1])

        return len(free_rooms)