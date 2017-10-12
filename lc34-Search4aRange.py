class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.binary_search(nums, target) 
        end = self.binary_search(nums, target+1)
        try:
            ans = [start if nums[start] == target else -1 , end-1 if nums[end-1] == target else -1  ]
        except Exception:
            ans = [-1, -1]
        
        return ans
    
    def binary_search(self, nums, target):
        lo = 0
        hi = len(nums)
        while lo<hi:
            mid = (int)(lo+hi)/2
            if nums[mid]>=target:
                hi = mid
            else:
                lo = mid + 1
        return lo
