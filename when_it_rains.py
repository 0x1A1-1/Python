'''
Created on Mar 25, 2016

@author: Cigarent
'''
def answer(heights):
    #implement function
    if len(heights)<=3:
        return 0
    rain = 0
    for i in range(0, len(heights)):
        prev = i - 1 if i!=0 else 0
        nxt = i + 1 if i!=len(heights)-1 else len(heights)-1
        while heights[prev]<heights[i] and prev>0:
            prev = prev - 1
        while heights[nxt]<heights[i] and nxt<len(heights)-1:
            nxt = nxt + 1
        #print("for ",i,"th, the prev and nxt is", prev, " , ",nxt)
        if prev != 0 or heights[prev]>heights[i]:
            #print("here")
            rain += heights[i]*(i-prev)-sum(heights[prev+1:i+1])
            #print("rain here PREV", heights[i]*(i-prev),sum(heights[prev+1:i+1]))
            #print("rain here", rain, heights[i]*(i-prev+1)," ",sum(heights[prev:i+1]))
            for x in range(prev+1, i):
                heights[x]=heights[i]
        if nxt != len(heights)-1 or heights[nxt]>heights[i]:
            rain += heights[i]*(nxt-i)-sum(heights[i:nxt])
            #print(heights[i]*(nxt-i)-sum(heights[i:nxt]))
            #print("rain here nxt", rain, heights[i]*(nxt-i)," ",sum(heights[i:nxt]))
            for x in range(i+1, nxt):
                heights[x]=heights[i]
        #print("after this round", heights)
    return rain
print(answer([3,2,1,1,3,1,5]))