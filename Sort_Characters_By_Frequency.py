class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for char, time in  collections.Counter(s).most_common():
            temp = char * time
            res += temp
        return res
