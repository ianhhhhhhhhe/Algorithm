class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        nums.sort()
        res = 1
        for i in nums:
            if i == res:
                res += 1
        return res
