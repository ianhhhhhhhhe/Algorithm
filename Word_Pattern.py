class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return map(pattern.find, pattern) == map(str.split().index, str.split())
