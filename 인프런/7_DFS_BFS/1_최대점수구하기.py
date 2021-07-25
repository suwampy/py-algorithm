def DFS(L,sum,time):
    global res

    if time>m:
        return

    if L == n:
        if sum>res:
            res=sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L]) #푼다
        DFS(L+1, sum, time) #안푼다


if __name__ == "__main__" :
    n,m = map(int,input()) # n: 문제으 ㅣ개수 m: 제한시간
    pv=list() # 문제 점수
    pt=list() # 문제 시간
    for _ in range(n):
        a,b = map(int, input().split())
        pv.append(a)
        pt.append(b)

    res=-2147000000
    DFS(0,0,0) # Level, 총점, 시간
    print(res)