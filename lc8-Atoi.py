import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strip_str = str.strip()
        
        if len(strip_str) == 0:
            return 0
        
        positive = 1
        if strip_str[0] == "-":
            positive = -1
            strip_str = strip_str[1:]
        elif strip_str[0] == "+":
            strip_str = strip_str[1:]
            
        result = re.findall("^[0-9]*", strip_str)[0]
        
        if len(result) == 0:
            return 0
        else: 
            return_int = int(result) * positive
        
        return_int = 2147483647 if return_int > 2147483647 else return_int
        return_int = -2147483648 if return_int < -2147483648 else return_int
        
        return return_int
