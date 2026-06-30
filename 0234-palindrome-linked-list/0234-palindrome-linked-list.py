# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
            
        # Step 1: Find the middle using Fast/Slow pointers
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: Compare the first half and the reversed second half
        left = head
        right = prev # prev is now the head of the reversed half
        
        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True

        