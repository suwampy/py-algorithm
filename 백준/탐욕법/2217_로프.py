def 로프():
    n = int(input())
    list=[]
    for _ in range(n):
        list.append(int(input()))

    list.sort(reverse=True)
    # input 15 10
    # 15*1 10*2
    # 15 20
    res = 0
    # n번쨰 큰 수 * n이 최대값이 되는 수
    for i in range(n):
        if res < list[i]*(i+1):
            res = list[i]*(i+1)

    print(res)

if __name__ == "__main__":
    로프()