class Solution(object):
	'''zigzag convertion'''
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zz = []
    	row = 0
    	inc = -1
    	if numRows == 1:
    	    return s
    	for n in range(numRows):
    		zz.append("")
    	for char in s:
    		zz[row]+=char
    		if row == 0 or row == numRows - 1:
    			inc *= -1
    		row+=inc
    	return "".join(zz)
