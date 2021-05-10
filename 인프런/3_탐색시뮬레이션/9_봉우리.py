import sys

def 봉우리():
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 가장자리 0으로 초기화
    a.insert(0,[0]*n)
    a.append([0]*n)

    for x in a:
        a.insert(0,0)
        a.append(0)

    # 탐색
    cnt = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            # all : 조건이 모두가 참일때 참
            if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
                cnt+=1


if __name_ == "__main__":
    봉우리()