import re

line = "My 2 favorite number is 7 and 16"
y = re.findall('[0-9]+', line)
print y
y = re.findall('[ABCDE]+', line)
print y
y = re.findall('[MYKy]+', line)
print y

#extract email address
line = "From cigarent.bang@wisc.edu Sat Jan 5 09:14:16 2016"
y = re.findall('\S+@\S+', line)
print y
y = re.findall('\S*@\S*', line)
print y

#what if I want something start with a From
#parentheses are not part of the match but they tell where to start and stop
y =  re.findall('^From (\S*@\S*)', line)
print y
y =  re.findall('^From \S*@\S*', line)
print y

#if I wanna get domain
y = re.findall('^From.*@(\S+)', line)
print y
y = re.findall('@([^ ]*)', line)
print y
