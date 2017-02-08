class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, current, n, i = 0, 0, 0, 0
        while current < len(nums)-1:
            while i <= last:
                current = max(i+nums[i],current)
                i+=1
            if last == current:
                return False
            last = current
            n += 1
        return n
