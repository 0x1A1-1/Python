string = raw_input()

#initial count
count = 0

#status bit to count for consecutive spaces
status = False

#Method 1
for i in range(0, len(string)-1):
    if string[i] ==" " or string[i]=="\t" or string[i]=="\n":
        if status:
            status=False
            count+=1
    else:
        status = True

print count+1

# Method 2
# list = string.replace("\\t"," ").replace("\\n", " ").split()
#
# print len(list)
#
#
# str = raw_input()

# count = 0
#
# isInWord = True
#
# for i in range(0, len(str)-1):
#     if isDelim(str[i]):
#         if isInWord:
#             isInWord = False
#             count +=1
#     else:
#         isInWord True
