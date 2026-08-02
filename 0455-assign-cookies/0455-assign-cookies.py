class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        left=0
        count=0
        right=0
        while left<len(g) and right<len(s):
            if g[left]<=s[right]:
                count+=1
                left+=1
            right+=1
        return count

        