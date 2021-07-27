## https://www.acmicpc.net/problem/2667
import sys
def DFS(x,y):
    global cnt
    a[x][y]='0' # 현재 방문 좌표 0으로 (재방문 x)

    cnt+=1
    for i in range(4): #상, 하, 좌, 우 반복
        nx = x+ dx[i]
        ny = y+ dy[i]

        if nx < 0 or nx >= n or ny <0 or ny >=n:
            continue
        if a[nx][ny] == '1': #1인경우 다시 재귀 돌아서 카운트 계쏙 올려주기~
            DFS(nx,ny)


if __name__ == "__main__":
    # 좌표문제는 dx, dy 리스트 선언해주자
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    n = int(input())
    a=[list(sys.stdin.readline()) for _ in range(n)]
    cnt=0
    apt=[]

    # a[x][y] 를 0,0부터 n,n 까지 비교해준다
    # a[i][j] == 1 일 경우만 cnt를 0으로 대입한 후 dfs(i,j) 실행
    for i in range(n):
        for j in range(n):
            if a[i][j] == '1':
                cnt=0
                DFS(i,j)
                apt.append(cnt)

    print(len(apt))
    apt.sort()
    for i in apt:
        print(i)

