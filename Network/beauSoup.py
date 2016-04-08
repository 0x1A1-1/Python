import urllib
from bs4 import BeautifulSoup

url = raw_input('Link? - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#retrieve a list of the anchor tags
#each tags is like a dic of HTML attributes

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
