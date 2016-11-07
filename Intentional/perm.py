from itertools import permutations

list1=[1,2,3]

print list(permutations(list1))

def toString(List):
    return ''.join(List)

def perm(list1, index, size):
    if index==size:
        print toString(list1)
    else:
        for i in range(index, size):
            list1[index], list1[i]= list1[i], list1[index]
            perm(list1, index+1, size)
            list1[index], list1[i]= list1[i], list1[index]

string = "ABC"
n = len(string)
a = list(string)
perm(a, 0, n)
