import json
merge='''
{
"strikers": [
{ "name": "Alexis Sanchez", "club": "Manchester United" },
{ "name": "Robin van Persie", "club": "Feyenoord" },

{ "name": "Nicolas Pepe", "club": "Arsenal" },
 
{ "name": "Gonzalo Higuain", "club": "Napoli" },
{ "name": "Sunil Chettri", "club": "Bengaluru FC" }
] }'''

data1=json.loads(merge)

print(data1)