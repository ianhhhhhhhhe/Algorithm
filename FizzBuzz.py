class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        t3 = 0
        t5 = 0
        ans = []
        for i in range(1, n+1):
            t3 += 1
            t5 += 1
            if t3 == 3 and t5 != 5:
                ans.append("Fizz")
                t3 = 0
                continue
            if t3 == 3 and t5 == 5:
                ans.append("FizzBuzz")
                t3, t5 = 0, 0
                continue
            if t5 == 5:
                ans.append("Buzz")
                t5 = 0
                continue
            ans.append(str(i))
        return ans
