def answer(str_S):
    # your code here
    S = int(str_S)
    load = 0
    while check(load)<=S and check(load+1)<=S:
        load+=500
    print(load)
    all = [ check(i) for i in range(load,load+5000)]
    if S in all:
        return str( load-500+[i for i,x in enumerate(all) if x==S].pop() )
    else:
        return "None"
        
def check(s):
    if s==0:
        return 1
    elif s==1:
        return 1
    elif s==2:
        return 2
    even = float(s)/2
    if even == int(even):
        return int(check(even) + check(even+1) + even)
    else:
        odd = (s-1)/2
        return int(check(odd-1) + check(odd) +1)
print(check(36695))
x="156559"
myans= answer(x)
print(myans)
if myans!="None":
    print(check(int(myans))) 