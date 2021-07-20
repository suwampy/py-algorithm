import sys
input = sys.stdin.readline

def DFS(L):
    if L == m:
        # res 출력
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    ## 레벨 = n
    ## m은 뻗어나가는 트리의 수인가?
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
