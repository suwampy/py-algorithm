def DFS(L,sum):
    global cnt

    if sum>T:
        return
    if L==k:
        if sum==T:
            cnt+=1
    else:
        for i in range(n[L]+1):
            DFS(L+1,sum+(p[L]*i))

if __name__=="__main__":
    T=int(input()) #지폐의금액
    k=int(input()) #동전의 가지 수

    cnt=0
    p=[]
    n=[]
    for _ in range(k):
        a,b = map(int,input().split())
        p.append(a)
        n.append(b)

    DFS(0,0,0)