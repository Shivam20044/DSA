class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if (len(s)!=len(goal)):
            return False
        sum=s+s
        if goal not in sum:
            return False
        else:
            return True
        