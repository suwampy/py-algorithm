import sys

def 수들의합():
    print()
    n,m = map(int,input().split())
    a = list(map(int,input().split()))

    # 초기 리스트
    #          lt rt
    #         tot
    # index |  0  1  2  3  4  5  6  7
    # list  | [1, 2, 1, 3, 1, 1, 1, 2]
    lt=0
    rt=1
    tot=a[0] # 연속 부분의 합. lt~ rt 바로 전의 합
    cnt=0 # 경우의 수 카운트

    while True:
        if tot<m:
            # tot가 m(합) 보다 작을 때
            if rt<n:
                # n에 가 있지 않을 때
                tot+=a[rt] #tot의 범위를 넓힌다
                rt+=1 #rt를 이동한다
            else:
                #rt가 n에 가있다...더할게없다 (끝지점 도달)
                break
        elif tot==m:
            # tot가 m(합)과 같을 때 = 목표 지점
            # 경우의 수 올려주기
            cnt+=1
            tot-=a[lt]
            lt+=1
        else:
            # tot가 m(합) 보다 클 때
            tot-=a[lt]
            lt+=1

    print(cnt)



if __name__ == "__main__":
    수들의합()