##Iternative

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n
        found = False
        def check(x):
            return ((1 + x)*x)/2
        while first<=last and not found:
            midpoint=(first+last)//2
            if check(midpoint) == n:
                return midpoint
            elif check(midpoint) < n:
                if check(midpoint+1)>n:
                    found = True
                    return midpoint
                else:
                    first = midpoint+1
            else:
                last = midpoint-1
