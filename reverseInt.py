class Solution(object):
	"""
	:type x: int
	:rtype: int
	"""
    def reverse(self, x):
	"""
	:type x: int
	:rtype: int
	"""
	rev = ""
	rev = str(x)
	rev=rev[::-1]
	if x>= 0 :
	    if int(rev) > 2147483647:
	        return 0
	    return int(rev)
	else:
	    if -1*int(rev[:-1]) < -2147483647:
	        return 0
	    return -1*int(rev[:-1])

'''Sol 2  68ms...slightly improve'''
def reverse(self, x):
	res = 0
    	sign = -1 if x<0 else 1
    	x=abs(x)
    	while x!=0:
    		res = res*10 + x%10
    		x/=10
    	if res < 2147483647 and res>-2147483647:
    		return sign*res
    	return 0

