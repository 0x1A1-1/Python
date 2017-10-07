def nextGreaterElement(self, findNums, nums):
	"""
	:type findNums: List[int]
	:type nums: List[int]
	:rtype: List[int]
	"""
	ans = []
	for i in findNums:
	    index = nums.index(i)
	    curr_loop = True
	    for j in nums[index:]:
		if j>i:
		    ans.append(j)
		    curr_loop = False
		    break
	    if curr_loop:
		ans.append(-1)
	    
	return ans
