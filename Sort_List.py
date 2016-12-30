class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        vals=[]
        while temp:
            vals.append(temp.val)
            temp = temp.next
        vals.sort()
        temp2=head
        for count in range(len(vals)):
            temp2.val = vals[count]
            temp2 = temp2.next
        return head
