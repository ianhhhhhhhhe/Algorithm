class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [1]*len(ratings)
        l = r = 1

        for i in range(1, len(ratings)):
            l = l + 1 if ratings[i] > ratings[i-1] else 1
            res[i] = l

        for i in range(len(ratings)-2, -1, -1):
            r = r + 1 if ratings[i] > ratings[i+1] else 1
            res[i] = max(r, res[i])

        return sum(res)
