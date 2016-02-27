'''
Created on Feb 26, 2016
There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity 
should be O(log (m+n)).
@author: Cigarent
'''
'83%'
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        overall = nums1 + nums2
        overall.sort()
        lenth = len(overall)
        if (lenth%2 ==0):
            return float(overall[lenth/2-1]+overall[lenth/2])/2
        else:
            return overall[(lenth-1)/2]