import sys

def 곳감():
    n = int(sys.stdin.readline())
    a=[list(map(int,input().split())) for _ in range(n)]

    m = int(sys.stdin.readline())

    # 밀기
    for i in range(m):
        # h = 행 번호
        # t = 방향
        # k개
        h, t, k =map(int, input().split())
        if t == 0:
            # 왼쪽
            for _ in range(k):
                # 회전 = pop 과 append를 이용하자!!
                # pop=꺼냄
                # append=끝에넣음
                a[h-1].append(a[h-1].pop(0))
        else:
            #오른쪽
            for _ in range(k):
                # insert = n번 인덱스에다가 넣는다다
               a[h-1].insert(0, a[h-1].pop())

    # 모래시계만들기
    res = 0
    s = 0
    e = n-1
    for i in range(n):
        for j in range(s, e+1):
            res+=a[i][j]
        if i<n//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1




if __name__ == "__main__":
    곳감()