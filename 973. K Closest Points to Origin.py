from collections import defaultdict
import math
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        d = defaultdict(list)
        for point in points:

            d[math.sqrt((point[0] * point[0]) + (point[1] * point[1]))].append(point)

        d = sorted(d.items())
        # print(d)
        res = []
        count = 0
        for tuples in d:
            count += 1
            res += tuples[1]
            if count == K:
                res = res[:K]
                return res
        res = res[:K]
        return res