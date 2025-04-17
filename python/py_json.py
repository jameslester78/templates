import json


#handling non ascii charecters in the json.dumps function

value = 'Ï'

j = {'x':value}

j1 = json.dumps(j, ensure_ascii=False)
j2 = json.dumps(j)

print (j1)
print (j2)