# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head.next is None:
            return True
        list1=[]
        temp=head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        list2=list1[:]
        list1.reverse()
        for i in range(len(list1)):
            if list1[i]!=list2[i]:
                return False
                break
        return True


        