class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums[::2], nums[1::2] = nums[:len(nums[::2])][::-1], nums[len(nums[::2]):][::-1]
