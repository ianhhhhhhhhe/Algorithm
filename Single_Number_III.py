class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = list(set(nums))*2
        for i in nums:
            res.remove(i)
        return res
