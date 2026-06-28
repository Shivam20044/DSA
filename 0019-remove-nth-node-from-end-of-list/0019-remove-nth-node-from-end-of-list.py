# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp=head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        if count==n:
            head=head.next
            return head
        stop_pos=count-n
        temp=head
        c=1
        while c<stop_pos:
            temp=temp.next
            c+=1
        temp.next=temp.next.next
        return head

        
        
        