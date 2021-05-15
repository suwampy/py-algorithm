import sys

def 정수제곱근():
    n = int(input())

    lt = 1
    rt = n
    res = 0

    while lt<=rt :
        mid = (lt+rt)//2
        if mid*mid <= n:
            lt = mid +1
        else:
            rt = mid - 1
            res = mid
    print(res)


if __name__ =="__main__":
    정수제곱근()