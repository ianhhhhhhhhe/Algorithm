class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(nums).lstrip('0') or '0'

class Solution2:
    # Python 3 version
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        from functools import cmp_to_key
        nums = [str(x) for x in nums]
        nums = sorted(nums, key=cmp_to_key(lambda x,y: int(y+x)-int(x+y)))
        return ''.join(nums).lstrip('0') or '0'
