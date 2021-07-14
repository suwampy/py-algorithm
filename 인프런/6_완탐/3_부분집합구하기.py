def DFS(v):
    if v ==  n+1:
        # 끝까지 왔을 때 출력
        for i in range(1, n+1):
            if ch[i] == 1: ## 부분집합인것만 출력
                print(i, end=' ')
        print()
    else:
        # 사용한다 사용하지 않는다 재귀 돌기
        # 사용한다 재귀
        ch[v] = 1
        DFS(v+1)

        # 사용하지 않는다 재귀
        ch[v] = 0
        DFS(v+1)
'''
          D(1) 부분집합으로 . . .
   사용한다↙     ↘사용하지않는다

'''

if __name__ == "__main__":
    n = int(input())
    ch=[0]*(n+1) # [0] [0] [0]
    DFS(1)