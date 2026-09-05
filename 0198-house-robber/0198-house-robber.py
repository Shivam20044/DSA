class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev=nums[0]
        prev2=0
        for index in range(1,len(nums)):
            if index>1:
                pick=nums[index]+prev2
            else:
                pick=nums[index]
            not_pick=prev
            curr=max(pick,not_pick)
            prev2=prev
            prev=curr
        return prev
        