##Iternative
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        bad = False
        while first<=last and not bad:
            midpoint = (first+last)//2
            if isBadVersion(midpoint):
                if not isBadVersion(midpoint-1):
                    return midpoint
                else:
                    last=midpoint-1
            else:
                first = midpoint+1
