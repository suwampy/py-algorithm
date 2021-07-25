'''
인접행렬 : 행->열
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    g=[[0]*(n+1) for _ in range(n+1)] # 그래프 0으로 초기화

    # 간선정보로 인접행렬 만들기
    for i in range(m):
        # 무방향 그래프
        '''
        a, b = map(int, input().split())
        g[a][b]=1
        g[b][a]=1
        '''

        # 가중치 방향 그래프
        a, b, c = map(intn, input().split())
        g[a][b]=c

    # 그래프 출력
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(g[i][j], end=' ')
        print()