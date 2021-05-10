import sys

def 격자판최대합():

    n = int(sys.stdin.readline())
    a=[]
    a=[list(map(int,input().split())) for _ in range(n)]

    largest = -2147000000

    # 행렬의 합
    for i in range(n):
        sum1=sum2=0 #행의 합, 열의 합
        for j in range(n):
            sum1+=a[i][j] # 행의 합
            sum2+=a[j][i] # 열의 합
        if sum1>largest:
            largest=sum1
        if sum2>largest:
            largest=sum2
    sum1=sum2=0
    #대각선의 합
    for i in range(n):
        sum1+=a[i][i] #대각선
        sum2+=a[i][n-i-1] #역대각선
        if sum1>largest:
            largest=sum1
        if sum2>largest:
            largest=sum2

if __name__ == "__main__":
    격자판최대합()