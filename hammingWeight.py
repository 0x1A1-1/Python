"""
count the number of bits of "1" in a unsigned number 
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n>0:
            count += n%2
            n=int(n/2)
        return count