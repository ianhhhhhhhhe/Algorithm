class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        num = 0
        for i in t:
            if i in s:
                if i == s[0]:
                    s = s[1:]
        return not len(s)
