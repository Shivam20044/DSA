class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # p1 points to the last valid number in nums1
        p1 = m - 1
        
        # p2 points to the last number in nums2
        p2 = n - 1
        
        # p points to the very last open slot in nums1
        p = m + n - 1
        
        # 1. Compare from the back and place the largest number at the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # 2. Sweep up any remaining elements from nums2
        # (If p1 has elements left, we don't need to do anything because 
        # they are already sitting in the correct spot at the front of nums1!)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1