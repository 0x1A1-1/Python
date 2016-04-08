import xml.etree.ElementTree as ET

#Just pretend that I'm a lil XML file
data = '''
<person>
  <name>Cig</name>
  <phone type="intl">
     +1 608 422 4456
   </phone>
   <email hide="yes"/>  #self closing tag
</person>'''

tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')
print 'Phone:',tree.find('phone').text.strip()

userList = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

user = ET.fromstring(userList)
userList = user.findall('users/user')
print 'User:count=',len(userList)

for item in userList:
    print 'X:',item.get('x')
    print 'ID:',item.find('id').text #item.get('id').text won't work, get Attr
    print 'name:',item.find('name').text
