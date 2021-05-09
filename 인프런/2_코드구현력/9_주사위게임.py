import sys

def 주사위게임():
    n = int(sys.stdin.readline())
    res=0
    for i in range(0,n):
        tmp = input().split()
        tmp.sort()
        a,b,c =map(int,tmp)
        if a==b and b==c:
            # a=b=c
            money=10000+a*1000
        elif a==b or a==c:
            money=1000+(a*100)
        elif b==c:
            money=1000+(b*100)
        else:
            money=c+100
        # 가장 큰 상금
        if money>res:
            res=money

if __name__ == "__main__":
    주사위게임()