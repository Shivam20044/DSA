class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for ch in s:
            if ch=="(" or ch=="[" or ch=='{':
                stack.append(ch)
            
            else:
              if len(stack)==0:
                return False
              chh=stack.pop()
              if (
                 (ch==")" and chh=="(")
                 or (ch=="}" and chh=="{")
                 or (ch=="]" and chh=="[")
              ):
                 continue
              else:
                return False
        return len(stack)==0
           
            
    

        