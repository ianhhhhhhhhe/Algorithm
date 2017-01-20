class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = temp = 0
        for i in nums:
            if i == 0:
                if max < temp:
                    max = temp
                temp = 0
            else:
                temp += 1
        return max if max > temp else temp
