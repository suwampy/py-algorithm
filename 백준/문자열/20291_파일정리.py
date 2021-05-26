n = int(input())

f = dict()

for _ in range(n):
  tmp = input().split('.')[1]
  if not tmp in f :
    f[tmp] = 1
  else :
    f[tmp] +=1

res = sorted(f.items())

for key, value in res:
    print(key.rstrip(), value)

