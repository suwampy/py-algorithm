def ATM():
    n = int(input())  # 사람의 수

    t = list(map(int, input().split()))  # 각 사람이 돈을 인출하는데 걸리는 시간

    t.sort()
    res = 0

    for i in range(n):
        for j in range(i + 1):
            print(res)
            res += t[j]

    print(res)
if __name__=="__main__":
    ATM()