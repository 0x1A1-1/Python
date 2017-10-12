class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        pivot  = self.binary_search_pivot(nums)
        if nums[-1] >= target:
            index = self.binary_search(nums[pivot:],target)+pivot
        else:
            index = self.binary_search(nums[:pivot],target)
        
        return index if index!=-1 and nums[index] == target else -1
        
    def binary_search(self, nums, target):
        if len(nums) == 0:
            return -1
        
        lo = 0 
        hi = len(nums) -1
        
        while lo<hi:
            mid = (int) (lo+hi)/2
            if nums[mid] < target:
                lo = mid +1
            elif nums[mid] >= target:
                hi = mid
        
        return lo
        
    def binary_search_pivot(self, nums):
        lo = 0
        hi = len(nums) - 1
        
        while lo<hi:
            mid = (int) (lo+hi)/2
            if nums[mid] < nums[0]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid+1
            else:
                break
        
        return lo
        
