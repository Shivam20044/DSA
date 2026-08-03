class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_indx=0
        for i in range(0,len(nums)):
            if i>max_indx:
                return False
            max_indx=max(max_indx,i+nums[i])
        return True
        