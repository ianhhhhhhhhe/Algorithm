class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res , temp = [], set()
        for i in nums:
            if not i in temp:
                temp.add(i)
            else:
                res.append(i)
        return res
