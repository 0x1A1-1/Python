class Solution(object):
     def threeSumClosest(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            nums.sort()
            nnum=len(nums)
            ans =  nums[0]+ nums[1]+ nums[2]
            for i in range(nnum-2):
                j = i+1
                k = nnum - 1
                while (j<k):
                    sum3 = nums[i]+ nums[j]+ nums[k]
                    if sum3 == target:
                        return sum3
                    if abs(sum3-target) < abs(ans-target):
                        ans=sum3
                    if sum3>target:
                        k-=1
                    else:
                        j+=1;
            return ans