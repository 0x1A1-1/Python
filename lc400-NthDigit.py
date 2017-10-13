import math

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        limit = 1
        lookup = {0:0}
        while limit < 10:
            lookup[limit] = int(9 * limit * math.pow(10, limit-1)  + lookup[limit-1])
            limit += 1 
            
        print lookup
        level = 0
        for i in lookup:
            if i+1 in lookup:
                if lookup[i] < n and lookup[i+1] >= n:
                    level = i
                    break
            else:
                level = i
        
        curr_n = n-lookup[level]-1
        count = curr_n / (level+1)
        off =  curr_n % (level+1)
        
        digit = (int)((str)(math.pow(10, level)+count)[off]) if level>0  else n
        
        return digit
        
