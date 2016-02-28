class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        string = str(x)
        revstring = string[::-1]
        print (revstring)
        return string == revstring
