'''
Created on Feb 26, 2016

@author: Cigarent
'''
'''
this answer exceed time limit of leetode
'''
class Solution(object):
    def longestPalindrome(self, s):
        def ispal(self, s):
            if (s==s[::-1]):
                return True
            else:
                return False
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        if (len(s)==1):
            return s
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if (ispal(object,s[i:j+1])):
                    if (len(s[i:j+1])>len(longest)):
                        longest=s[i:j+1]
        return longest   
    longestPalindrome(object, "a")
