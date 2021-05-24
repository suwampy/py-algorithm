n = int(input())

l = list(map(int,input().split()))
l.sort(reverse=True)

res = l[0]

for i in range(1,n):
  res += l[i]/2

print('%g'%res)

