class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in nums[:]:
            if i == val:
                nums.remove(val)
        return len(nums)

class Solution2(object):
    # An unusual way but it works!
    def removeElement(self, nums, val):
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)
