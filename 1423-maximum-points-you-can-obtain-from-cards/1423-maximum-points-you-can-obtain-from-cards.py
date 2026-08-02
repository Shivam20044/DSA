class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left_sum=0
        if len(cardPoints)==k:
            return(sum(cardPoints))
        for i in range(0,k):
            left_sum+=cardPoints[i]
        
        right_sum=0
        right_indx=len(cardPoints)-1
        maxi=left_sum
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_indx]
            maxi=max(maxi,left_sum+right_sum)
            right_indx-=1
        return maxi

        