'''
Created on Mar 25, 2016

@author: Cigarent
'''
def encode(message):
    # your code here
    ans = []
    ans.append( (129*message[0])%256 )
    for i in range(1, 16):
        ans.append( ((129 * message[i]) ^ message[i-1]) % 256 )
    return ans

def answer(digest):
    ans = []
    for m in range (0,16):
        prev = ans[m-1] if m!=0 else 0
        for i in range(0, 129):
            num =  ( (digest[m]+i*256) ^ prev )/129.0
            if num==int(num):
                ans.append(int(num))
    return ans
    

print(answer([0,129,3,129,7,129,3,129,15,129,3,129,7,129,3,129]))
print(encode([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(answer([0,129,5,141,25,137,61,149,113,145,53,157,233,185,109,165]))