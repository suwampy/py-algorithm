import sys

def 마구간정하기():

    n, c = map(int,input().split())

    list=[]
    for _ in range(n):
        temp = int(input())
        list.append(temp)

    list.sort()
    lt=1
    #최고점은 최대값
    rt=list[n-1]

    print(list)

    # 최고점이 좁혀질때까지
    while lt<=rt:
        mid=(lt+rt)//2
        # Count = 마구간에 들어갈수있는 말들의 수
        # 가  3마리보단 많아야함!
        if Count(mid,list,n)>=c:
            res=mid
            lt=mid+1
        else:
            rt=mid-1

    print(res)

def Count(len,list,n):
    # len = 최대값,최소값의 중간값
    # list = 좌표 리스트
    # n = 마구간의 수
    cnt=1
    ep=list[0] # end point

    for i in range(1, n):
        if list[i]-ep>=len:
            cnt+=1
            ep=list[i]
    return cnt


if __name__ =="__main__":
    마구간정하기()