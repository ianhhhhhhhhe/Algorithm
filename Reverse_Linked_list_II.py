# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        res = pre = self
        res.next = head

        for i in range(m - 1):
            pre = pre.next

        reverse = None
        curr = pre.next
        for i in range(n - m + 1):
            next = curr.next
            curr.next = reverse
            reverse = curr
            curr = next

        pre.next.next = curr
        pre.next = reverse

        return res.next
