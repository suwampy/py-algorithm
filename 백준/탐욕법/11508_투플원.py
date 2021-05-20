def 투플원():
    n = int(input())
    l = []
    res = 0

    for _ in range(n):
        l.append(int(input()))

    l.sort(reverse=True)

    for i in range(2,len(l),3):
        res += l[i]

    print(sum(l)-res)

if __name__=="__main__":
    투플원()