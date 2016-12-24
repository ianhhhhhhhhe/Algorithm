class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        ok = [True]
        for i in range(1, len(s)+1):
            ok.append(any(ok[j] and s[j:i] in wordDict for j in range(i)))
        return ok[-1]
