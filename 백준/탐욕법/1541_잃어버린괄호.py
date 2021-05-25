s = input().split('-')
l =[]
for i in s:
    tmp = 0

    s = i.split('+')

    for j in s:
      tmp += int(j)
    
    l.append(tmp)

res=l[0]

for i in range(1,len(l)) :
    res-=int(l[i])

print(res)