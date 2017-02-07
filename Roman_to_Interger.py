class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        last = s[0]
        for i in s[1:]:
            if roman[last] < roman[i]:
                z -= roman[last]
            else:
                z += roman[last]
            last = i
        return z + roman[last]
