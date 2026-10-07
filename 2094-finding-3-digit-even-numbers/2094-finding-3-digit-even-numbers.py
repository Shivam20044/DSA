class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = set()
        n = len(digits)
        
        for i in range(n):
            if digits[i] == 0:
                continue  # Leading digit cannot be 0
            for j in range(n):
                if j == i:
                    continue  # Cannot reuse the same element
                for k in range(n):
                    if k == i or k == j:
                        continue  # Cannot reuse elements
                    if digits[k] % 2 == 0:
                        res.add(digits[i] * 100 + digits[j] * 10 + digits[k])
                        
        return sorted(res)