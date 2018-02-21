###Iternative
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        found = False
        while first<=last and not found:
            midpoint = (first + last)//2
            if guess(midpoint) == 0:
                found = True
            else:
                if guess(midpoint)==-1:
	                last = midpoint-1
                else:
                    first = midpoint+1
        return midpoint
