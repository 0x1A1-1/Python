def lia(arr):
	if not arr:
	  return 0
	if len(arr) == 1:
	  return 1

	start = 0 
	end = 1
	max_len = 1
	while end < len(arr):
	  if arr[end] > arr[end-1]:
	    if end-start+1 > max_len:
	      max_len = end-start+1
	  else:
	    start = end
	  end += 1
	return max_len



print lia([1,2,3,2,4,5,6])
