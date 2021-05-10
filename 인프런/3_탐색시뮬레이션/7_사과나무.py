import sys

def 사과나무():
    n = int(sys.stdin.readline())
    a=[]
    a=[list(map(int,input().split())) for _ in range(n)]

    res=0
    #처음중간지점
    s=e=n//2

    for i in range(n):
        for j in range(s,e+1):
            res+=a[i][j]
        if i<n//2:
            #퍼지기
            s-=1
            e+=1
        else:
            #작아지기
            s+=1
            e-=1


if __name__ == "__main__":
    사과나무()