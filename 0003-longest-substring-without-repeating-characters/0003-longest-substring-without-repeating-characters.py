class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=0
        dictt={}
        maxi=0
        while r<len(s):
            if s[r] in dictt:
                l=max(l,dictt[s[r]]+1)
            
            maxi=max(maxi,r-l+1)
            dictt[s[r]]=r
            r+=1
        return maxi