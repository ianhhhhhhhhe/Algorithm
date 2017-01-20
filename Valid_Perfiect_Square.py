class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        max = num/2
        min = 1
        while max-min > 1:
            mid = (max + min)/2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                max = mid
            else:
                min = mid
        return min**2==num or max**2==num
