def quicksort(sortList):
    left=list()
    equal=list()
    right=list()

    if len(sortList)>1:
        pivot = sortList[0]
        for i in sortList:
            if i<pivot:
                left.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                right.append(i)
        return quicksort(left)+equal+quicksort(right)
    else:
        return sortList


#test
array=[12,4,5,6,7,3,1,15]
print quicksort(array)
