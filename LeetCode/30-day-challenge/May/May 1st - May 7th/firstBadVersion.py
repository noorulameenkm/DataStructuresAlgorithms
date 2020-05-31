# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        firstBad = None
        while start < end:
            mid = start + int((end - start) / 2)
            
            if isBadVersion(mid):
                firstBad = mid
                end = mid
            else:
                start = mid + 1
                
        if start == end:
            if isBadVersion(start):
                firstBad = start
            
        return firstBad
        
        
        
        