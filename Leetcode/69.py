##Iternative

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        first = 1
        last = x
        found = False
        if x ==0:
            return 0
        while first<=last and not found:
            midpoint = (first+last)//2
            if x/midpoint==midpoint:
                found=True
                return midpoint
            else:
                if x/midpoint>midpoint:
                    if x/(midpoint+1)<(midpoint+1):
                        found=True
                        return midpoint
                    else:
                        first = midpoint+1
                else:
                    last = midpoint-1
