sol = {0:1, 1:1, 2:2}

        
def check(s):
    global sol
    if s in sol:
        return sol[s]
    else:
        if s%2==0:
            sol[s] = check(s/2) + check(s/2 + 1) + s/2
        else:
            sol[s] = check((s-1)/2-1) + check((s-1)/2) + 1
    return sol[s]

def bin_search(f, s):
    start, end  = 0, s
    while start <= end:
        mid =(start +end)/2
        mid_val = check(f(mid))
        if mid_val == s:
            return mid
        elif mid_val<s:
            start = mid + 1
        else:
            end = mid - 1
    return -1
    
def answer(str_S):
    # your code here
    s = int(str_S)
    ans = []
    even = bin_search(lambda x: x * 2, s)*2
    odd =  bin_search(lambda x: x * 2 + 1, s)*2 + 1
    if even >= 0:
        ans.append(even)
    if odd >= 0:
        ans.append(odd)
    if len(ans)==0:
        return "None"
    else:   
        return str(max(ans))

    
print(check(65))
x="122"
myans= answer(x)
print(myans)