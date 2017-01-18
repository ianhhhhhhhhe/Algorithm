class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        try:
            while i < (len(nums) - 1):
                if nums[i] == nums[i+1] == nums[i+2]:
                    del nums[i]
                else:
                    i += 1
        finally:
            return len(nums)
