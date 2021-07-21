def DFS(L,sum): # L = 동전의 사용갯수
    global res

    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])


if __name__ == "__main__":
    n = int(input()) # 동전으 ㅣ종류 개수
    a = list(map(int,input().split())) # 동전의 종류
    m = int(input())
    res=2147000000
    a.sort(reverse=True)
    DFS(0,0)
    print(res)

