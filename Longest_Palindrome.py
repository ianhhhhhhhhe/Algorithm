class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s)
        return len(s) - max(len(tuple(v for v in d.values() if v % 2)) - 1, 0)
