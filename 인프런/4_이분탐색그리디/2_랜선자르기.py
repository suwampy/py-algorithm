import sys

def 랜선자르기():
    # 이분검색 = 결정 알고리즘에서 쓰임
    # 특징-> 답은 특정 범위에 있다는 걸 알 수 있다
    # 중앙값을 정해놓고 될수있냐 없냐 확인하는 함수 만들어서
    # 답이된다~ 범위를 좁힘ㅎㅎ
    k, n = map(int, input().split())
    Line = []
    res = 0
    largest=0
    for i in range(k):
        tmp=int(input())
        Line.append(tmp)
        # 범위 : 0 ~ 가장 큰 수로정해야하므로
        # 최대값산출
        largest= max(largest, tmp)

    # 이분검색 ㄱㄱ
    lt=1
    rt=largest

    while lt<=rt:
        mid=(lt+rt)//2 # mid = 랜선의 길이
        if Count(mid,Line) >= n:
            res = mid
            lt=mid+1
        else:
            rt=mid-1

    print(res)


def Count(len,Line):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt


if __name__ == "__main__":
    랜선자르기()