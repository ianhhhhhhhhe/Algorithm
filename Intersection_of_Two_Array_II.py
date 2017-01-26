class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])
