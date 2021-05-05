import sys

def k번째큰수():
    n , k = map(int, sys.stdin.readline().split())
    a = list(map(int, input().split()))

    ## 중복제거 = set
    res = set()

    ## 3장을 뽑을 수 있는 모든 경우
    for i in range(n):
        for j in range(i+1,n):
            for m in range(j+1,n):
                res.add(a[i]+a[j]+a[m])

    res = list(res)
    res.sort(reverse=True)
    print(res[k-1])

if __name__ == "__main__":
    k번째큰수()