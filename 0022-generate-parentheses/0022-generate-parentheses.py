class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        paran=['']*(n*2)
        result=[]
        def generatepara(index,total,paran,result):
            if index>=len(paran):
                if total==0:
                    result.append("".join(paran))
                return
            if total>len(paran)//2:
                return
            elif total<0:
                return
            paran[index]="("
            sum=total+1
            generatepara(index+1,sum,paran,result)
            paran[index]=")"
            sum=total-1
            generatepara(index+1,sum,paran,result)

        generatepara(0,0,paran,result)
        return result
        

        