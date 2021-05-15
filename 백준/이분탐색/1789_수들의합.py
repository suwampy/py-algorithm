import sys

def 수들의합():
    s = int(input())
    res = 0

    lt = 1
    rt = s

    while lt<=rt:
        mid=(lt+rt)//2
        # 1부터 mid까지 합이 s보다 작거나 같다면
        if mid * (mid+1) // 2 <= s:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)



if __name__ == "__main__":
    수들의합()