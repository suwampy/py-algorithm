def 알바생강호():
    n = int(input())
    res = 0

    l = []
    for _ in range(n):
        l.append(int(input()))

    l.sort(reverse=True)

    for i in range(n):
        if l[i] - i < 0:
            continue
        res += (l[i] - i)

    print(res)

if __name__ =="__main__":
    알바생강호()