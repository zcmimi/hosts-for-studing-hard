import os

res=[]

for i in os.listdir('.'):
    if not i.endswith(".list"):continue
    str=open(i,encoding="utf-8").read()
    list=str.split('\n')
    for j in list:
        print(j)
        val=j.split('#',1)[0]
        res.extend(val.split(' '))
print(res)