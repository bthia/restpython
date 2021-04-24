import json

a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionID":10892}]}'
#print(a_string)

d = json.loads(a_string)
print('--- example 1')
print(type(d))
print(d.keys)
print(d["resultCount"])

def pretty(obj):
  return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a':90, '5':50}, 'key2': {'b':3, 'c':"yes"}}

print('\n\n--- example 2 ---')
print(d)
print('---')
print(pretty(d))