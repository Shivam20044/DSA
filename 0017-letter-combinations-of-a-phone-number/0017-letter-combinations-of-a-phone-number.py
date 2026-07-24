class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictt={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result=[]
        def fun(index,subset):
            if index>=len(digits):
                result.append("".join(subset))
                return
            for ch in dictt[digits[index]]:
                subset.append(ch)
                fun(index+1, subset)
                subset.pop()
        fun(0,[])
        return result
        