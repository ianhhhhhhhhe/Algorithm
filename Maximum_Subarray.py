class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        curTemp = maxTemp = nums[0]
        for num in nums[1:]:
            curTemp = max(num, curTemp + num)
            maxTemp = max(maxTemp, curTemp)
        return maxTemp
