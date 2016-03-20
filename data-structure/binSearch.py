def binSearch(L, target):
	if L is None:
		return 
	int left = 0
	int right = L.len()
	while (left<right):
		(int)mid = (left+right)/2
		if (L[mid]==target):
			return mid
		elif (L[mid]>target):
			right = target -1
		else:	
			left = target +1
	print("Nothing's foudn")
	return
