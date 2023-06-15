import json

print(type("uk.json")) #'str'
f = open("uk.json")
print(type(f)) #'_io.TextIOWrapper'
print(f) #_io.TextIOWrapper name='uk.json' mode='r' encoding='UTF-8'

data = json.loads(f.read())
for colour in data:
    print(colour["color"])