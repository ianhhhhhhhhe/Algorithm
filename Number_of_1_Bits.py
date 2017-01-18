class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in bin(n):
            if i == '1':
                res += 1
        return resS
