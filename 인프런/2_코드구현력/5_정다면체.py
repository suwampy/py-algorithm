import sys

def 정다면체():
    n , m = map(int, input().split())
    cnt=[0]*(n+m+3) # 3 : 추가 여유 공간..
    max = -2147000000 # max는 제일 작은 값으로 설정해둔당.
    print(cnt)
    for i in range(1,n+1):
        for j in range(1,m+1):
            cnt[i+j]+=1

    # 최대값넣기
    for i in range(n+m+1):
        if cnt[i]>max:
            max=cnt[i]

    ## 최대값 출력하기
    for i in range(n+m+1):
        if cnt[i]==max:
            print(i, end=' ')

    print(cnt)


if __name__ == "__main__":
    정다면체()