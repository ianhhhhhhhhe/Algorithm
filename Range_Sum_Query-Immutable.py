class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums + [0]
        for i in xrange(len(self.nums)-2, -1, -1):
            self.nums[i] += self.nums[i+1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[i] - self.nums[j+1]

class NumArray2(object):
    # Very very slow
    def __init__(self, nums):
        self.nums = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j+1])
