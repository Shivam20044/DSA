# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count=0
        temp=head
        while head is not None:
            head=head.next
            count+=1
        
        val=0
        if count==1:
            return temp
        if count//2==0:
            while temp.next!=None and val<(count//2):
                temp=temp.next
                val+=1
            temp=temp.next
       
        else:
            while temp.next!=None and val<(count//2):
                temp=temp.next
                val+=1
        
        return temp


        