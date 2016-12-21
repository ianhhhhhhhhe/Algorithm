class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        n = 1
        l = len(nums)
        for i in range(l):
            out.append(n)
            n = n * nums[i]
        n = 1
        for i in range(l-1,-1,-1):
            out[i] = out[i] * n
            n *= nums[i]
        return out
