import json

jsonText = '''
{
  "name" : "Cig",
  "phone" : {
    "type" : "intl",
    "number" : "+1 608 422 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(jsonText)
print 'Name:', info["name"]
print 'Hide:', info["email"]["hide"]

#Array in JSON, list in python
input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(input)
print 'User count:', len(info)
for user in info:
    print "ID:",user["id"]
    print "Name:",user["name"]
