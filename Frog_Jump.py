class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        d = {x: set() for x in stones}
        d[1].add(1)
        for x in stones[:-1]:
            for j in d[x]:
                for k in [j-1, j, j+1]:
                    if k > 0 and x+k in d:
                        d[x+k].add(k)
        return bool(d[stones[-1]])
