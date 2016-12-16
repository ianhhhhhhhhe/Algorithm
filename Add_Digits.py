class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num/10 is 0:
            return num
        tmp = 0
        while num:
            tmp += num % 10
            num //= 10
        return self.addDigits(tmp)
