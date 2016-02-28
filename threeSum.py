'''
Created on Feb 28, 2016

@author: Cigarent
'''
class Solution(object):
        def threeSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            dict = {}
            ans = []
            if nums.count(0)>=3:
                ans.append([0,0,0])
            for i in nums:
                if i not in dict:
                    dict[i]=min(2, nums.count(i))
            
            newNums = []
            for i in dict:
                for n in range(dict[i]):
                    newNums.append(i)
            newNums.sort()
            nnum = len(newNums)
            for i in range(nnum-1):
                for j in range(i+1, nnum):
                    z= -(newNums[i]+newNums[j])
                    if z in dict: 
                        if z==newNums[i] or z==newNums[j]:
                            if dict[z]==2 and newNums[i]!=0 and newNums[j]!=0 :
                                ans.append([newNums[i],newNums[j],z])
                        else:
                            if dict[z]>=0:
                                ans.append([newNums[i],newNums[j],z])
            ret = []
            for i in ans:
                i.sort()
                if i not in ret:
                    ret.append(i)
                
            return ret
                
    threeSum(object,[-2,-1,0,0,0,1,2,5])