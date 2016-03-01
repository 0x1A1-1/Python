class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) < 1:
            return nums
        nums.sort()
        head = nums[0]
        tail = nums[0]
        ans = []
        if len(nums)==1:
            ans.append(str(head))
        else:
            for i in range(len(nums)):
                if head == nums[len(nums)-1]:
                    ans.append(str(head))
                    break
                if tail == nums[len(nums)-1]:
                     ans.append(str(head)+"->"+str(tail))
                     break
                if nums[i]+1 == nums[i+1]:
                    tail = nums[i+1]
                    continue
                elif head == tail:
                    ans.append(str(head))
                else:
                    ans.append(str(head)+"->"+str(tail))
                head = nums[i+1]
                tail = nums[i+1]
        return ans