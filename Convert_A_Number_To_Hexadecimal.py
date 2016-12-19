class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return hex(num if num>0 else 16**8+num)[2:]
