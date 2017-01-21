class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right-1:
            mid = (left + right)/2
            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid
            elif nums[mid] == nums[left]:
                left += 1
            else:
                right = mid
        return nums[left] if nums[left]<nums[right] else nums[right]
