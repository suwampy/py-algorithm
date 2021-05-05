import sys

def k번째약수():
    ## 풀이
    n , k = map(int, input().split())
    cnt = 0
    for i in range(1, n+1):
        if n % 1 == 0 :
            cnt+=1
        if cnt == k :
            print(i)
            break
    else :
        print(-1)

    ## 내가푼것
    # n = int(sys.stdin.readline())
    # m = []
    # for i in range(1,n+1):
    #     if n%i==0:
    #         m.append(i)
    #
    # k = int(sys.stdin.readline())
    # m.sort(reverse=True)
    #
    # if len(m)<=k:
    #     print('-1')
    # else:
    #     print(m[k])


if __name__ == "__main__":
    k번째약수()