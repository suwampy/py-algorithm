

def DFS(L, sum, tsum):
    global result
    print(L)
    if sum+(total-tsum) < result: # 가지뻗기 멈춰
        return

    if sum>c: #무게제한을 넘으면 안돼
        return
    if L == n : ## 말단노드. 종료지점
        if sum>result:
            print(sum)
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__ == "__main__":
    # n마리의 바둑이, 바둑이의 무게 w
    # c 이상이면 안됨!!

    c , n = map(int, input().split())
    a=[0]*n
    result = -2147000000

    for i in range(n):
        a[i]=int(input())

    total=sum(a)
    DFS(0,0,0)