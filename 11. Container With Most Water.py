class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        temp = 0
        while left < right:
            if height[left] <= height[right]:
                temp = height[left] * (right - left)
                left += 1
            elif height[left] >= height[right]:
                temp = height[right] * (right - left)
                right -= 1
            if temp > max_water:
                max_water = temp
        return max_water