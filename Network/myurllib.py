import urllib
import re

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

#print file
for line in fhand:
  print line.strip()

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
#count word
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print counts

fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    y=re.findall('href="(.*)"',line)
    if len(y)>0:
        url = y[0]
        print y
    else:
        continue
fhand = urllib.urlopen(url)
for line in fhand:
    print line.strip()
