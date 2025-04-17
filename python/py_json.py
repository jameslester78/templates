import json

value = 'Ï'

j = {'x':value}

j1 = json.dumps(j, ensure_ascii=False)
j2 = json.dumps(j)

print (j1)
print (j2)