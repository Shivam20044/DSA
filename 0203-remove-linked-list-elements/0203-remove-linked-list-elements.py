# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head is not None and head.val==val:
            head=head.next
        if head is None:
            return head
        temp=head
        while temp.next is not None:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
            
        return head