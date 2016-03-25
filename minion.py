"""verify a date. Origin and order"""
def answer(x, y, z):
    # your code here
    from itertools import permutations
    seq = list(permutations([x,y,z]))
    wrong =[]
    for x in seq:
        if x[0]>12 or x[1]>31:
            wrong.append(x)
        if x[0] in [4,6,9,11] and x[1]>30:
            wrong.append(x)
        if x[0]==2 and x[1]>28:
            wrong.append(x)
    ansSet = set([x for x in seq if x not in wrong])
    if len(ansSet) > 1:
        return "Ambiguous"
    date = next(iter(ansSet))
    date0 = "0"+str(date[0]) if date[0]<10 else str(date[0])
    date1 = "0"+str(date[1]) if date[1]<10 else str(date[1])
    date2 = "0"+str(date[2]) if date[2]<10 else str(date[2])
    return date0+"/"+date1+"/"+date2
print(answer(2,3,13))