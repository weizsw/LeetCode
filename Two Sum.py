class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        newnum = []
        for num in nums:
            newnum.append(num)
        newnum.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            if newnum[left] + newnum[right] == target:
                num1 = newnum[left]
                num2 = newnum[right]
                break
            elif newnum[left] + newnum[right] < target:
                left += 1
            else:
                right -= 1
        mylist = [0,0]


        for index in range(len(nums)):
            if nums[index] == num1:
                mylist[0] = index
            elif nums[index] == num2:
                mylist[1] = index

        return mylist

solution = Solution()
print(solution.twoSum([3,2,4],6))
