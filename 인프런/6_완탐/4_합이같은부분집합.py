if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)

def DFS(L, sum):
    if L == n :
        if sum == (total-sum):
            print('YES')
        else:
            DFS(L+1, sum+a[L]) # yes
            DFS(L+1, sum) #no