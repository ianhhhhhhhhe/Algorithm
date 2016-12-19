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
        count=0
        while temp2:
            temp2.val = vals[count]
            count+=1
            temp2 = temp2.next
        return head
