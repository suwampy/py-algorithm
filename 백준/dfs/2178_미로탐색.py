import sys
if __name__ == "__main__":

    dx = [-1,0,1,0]
    dy= [0,1,0,-1]

    n, m = map(int,sys.stdin.readline().split())
    a= [list(sys.stdin.readline()) for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if[i][j] == '1':
