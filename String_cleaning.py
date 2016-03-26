'''
Created on Mar 25, 2016

@author: Cigarent
'''
def answer(chunk, word):
    # your code here
    if chunk=="":
        return None
    if not word in chunk:
        return None
    resultSet = set()
    for i in range(0,len(chunk)-len(word)):
        piece = chunk
        index = piece.find(word,i)
        if index != -1:
            piece = remove(piece, word, index)
        resultSet.add(piece)
    result = [x for x in resultSet]
    result.sort(key=len)
    newResult = [x for x in result if len(x)==len(result[0])]
    newResult.sort()
    return newResult[0]
def remove(string, sub, index):
    print(string, sub, index)
    curr = string[:index]+string[index+len(sub):]
    newIn = curr.find(sub)
    if newIn!=-1:
        return remove(curr, sub, newIn)
    else:
        return curr
print(answer("goodgooogoogfogoood","goo"))