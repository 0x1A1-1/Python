from math import factorial

# def answer(seq):
#     if len(seq) <= 2:
#         return 1
#     else:
#         return helper(seq)
#     # your code here
# 
# def helper(seq):
#     if len(seq) < 2:
#         return len(seq)
#     else:
#         left = [x for x in seq if x>seq[0]]
#         right = [x for x in seq if x<seq[0]]
#         print(left, right)
#         if len(left)==0:
#             return helper(right)
#         elif len(right)==0:
#             return helper(left)
#         else:
#             print((len(right)+1)*len(left),len(left))
#             return helper(left)*helper(right)*combination((len(right)+1)*len(left)
#                                                       ,len(left))

# def combination(n,k):
#     print(n,k)
#     numerator=factorial(n)
#     denominator=(factorial(k)*factorial(n-k))
#     answer=numerator/denominator
#     return answer

#calculates n choose r
def choose(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

#recursive function that calculates the number of ways to rearrange the left and right subtrees such that the parent node still precedes them in the sequence
def answer(seq):
    if len(seq) <= 2:
        return 1
    else:
        left = [i for i in seq[1:] if i < seq[0]]
        right = [i for i in seq[1:] if i > seq[0]]
        return answer(left) * answer(right) * choose(len(seq) - 1, len(left))
print(answer([5, 9, 8, 2, 1]))
# print(answer([5,9,8,2,1]))
