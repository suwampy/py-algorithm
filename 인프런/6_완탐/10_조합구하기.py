def DFS(L,S):
    if L==m:
        for i in range(L):
            print(res[i], end=" ")
        print()
        #cnt+=1
    else:
        for j in range(S,n+1):
            res[L] = j
            DFS(L+1,j+1) # 가지뻗기하니깐...j+1해야함

if __name__ == "__main__":
    n ,m = map(int,input().split())
    res = [0]*(n+1)
    #cnt=0
    DFS(0,1)