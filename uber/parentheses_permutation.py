result = []
num = 0

def print_parentheses(left,right):
  global num
  global result

  if left == 0 and right == 0:
    print ''.join(result)
    return 

  pos = num -left - right
  if left>0:
    result[pos] ='('
    print_parentheses(left-1, right)

  if left<right:
    result[pos]=')'
    print_parentheses(left, right-1)

def print_all_perm(n):
  global num
  global result

  num = n*2
  result = [None] * num
 
  print_parentheses(n,n)

print_all_perm(3)
