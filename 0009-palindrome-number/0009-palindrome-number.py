class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        strr=str(x)
        return strr == strr[::-1]
        