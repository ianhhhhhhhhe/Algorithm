# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return
        p = head
        q = head

        while q and q.next:
            q = q.next.next
            p = p.next

        mid = p.next
        p.next = None
        begin = head
        end = mid
        pre = None

        while end:
            temp = end.next
            end.next = pre
            pre = end
            end = temp

        while pre and begin:
             a = pre.next
             b = begin.next
             begin.next = pre
             pre.next = b
             begin = b
             pre = a
        return
