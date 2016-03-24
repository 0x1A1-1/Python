"""
Given a non negative integer number num. For every numbers i in the range 0 ¡Ü i ¡Ü num calculate
 the number of 1's in their binary representation and return them as an array.
 
 Dynamic Programming
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0,1]
        logR = 0
        numS = num
        while numS>1:
            logR+=1
            numS/=2
        while logR>0:
            new = [ x+1 for x in result ]
            result.extend(new)
            logR-=1
        return result[:num+1]