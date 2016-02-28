class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
    	ns = str(num)
    	ls = []
    	ans = ""
    	dic = [["","","","M"],["CM","D","CD","C"],["XC","L","XL","X"],["IX","V","IV","I"]]
    	if len(ns)<4:
    		ns=(4-len(ns))*'0'+ns
    	for index, dig in enumerate(ns):
    		tempdig=int(dig)
    		if tempdig==9:
    			ls.append(dic[index][0])
    		elif tempdig>5:
    			ls.append(dic[index][1])
    			tempStr= dic[index][3] * (tempdig-5)
    			ls.append(tempStr)
    		elif tempdig==5:
    			ls.append(dic[index][1])
    		elif tempdig==4:
    			ls.append(dic[index][2])
    		else:
    			ls.append( dic[index][3] * tempdig)
    	for i in ls:
    	    ans+=i
        return ans
    
