import sys

def 두리스트합치기_n():
    n = int(input())
    a = list(map(int, input().split()))

    m =int(input())
    b = list(map(int, input().split()))

    #point 변수
    p1=p2=0
    c=[]

    #point가 끝까지 가면 끝~
    while p1<n and p2<m:
        if a[p1]<=b[p2]: # b 리스트의 p2 지점이 더 큰 경우
            c.append(a[p1]) #a리스트의 p1지점을 넣어준다
            p1+=1 # p1의 포인트지점을 1올린다
        else:
            c.append(b[p2])
            p2+=1

    # 남은부분 붙이기
    if p1<n:
        c=c+a[p1:]
    if p2<m:
        c=c+b[p2:]

    for x in c:
        print(x,end=' ')


def 두리스트합치기_nlogn():
    n = int(input())
    ln = list(map(int, input().split()))

    m =int(input())
    lm = list(map(int, input().split()))

    res = ln+lm

    # sort 함수 =>n log n
    # 이미 정렬되어있는 문제 => n 으로 끝낼 수 있음
    res.sort()

    for x in res:
        print(x,end=' ')

if __name__=="__main__":
    두리스트합치기_nlogn()