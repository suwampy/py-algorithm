import sys

def 뮤직비디오():
    # n개의 곡
    # m개의 dvd에 동영상을 녹화
    n,m=map(int,input().split())

    # 부른 곡의 길이
    a =list(map(int, input().split()))
    a.sort()
    res=0

    lt = 1
    rt = sum(a)

    while lt<=rt:
        mid=(lt+rt)//2
        if Count(mid,a)<=m:
            res = mid
            rt=mid-1
        else:
            lt=mid+1
    #종오오옷나 어렵다 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

    print(res)

def Count(len, list):
    cnt=1
    sum=0

    for a in list:
        if sum+a>=len:
            cnt+=1
            sum=a # 인덱스값으로 초기화~
        else:
            sum+=a

    print("cnt",cnt)
    return cnt





if __name__ == "__main__":
    뮤직비디오()