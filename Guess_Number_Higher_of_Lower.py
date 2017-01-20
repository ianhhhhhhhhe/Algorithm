# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        big =  n
        sma = 0
        while sma < big:
            mid = (sma + big)/2
            if guess(mid) == 1:
                sma = mid + 1
            else:
                big = mid
        return sma
