import sys

def 뒤집은소수():
    n=int(sys.stdin.readline())
    a = list(map(int, input().split()))
    for x in a:
        tmp=reverse(x)
        print(tmp)
        if isPrime(tmp):
            print(tmp, end=' ')

# 뒤집는 함수
def reverse(x):
    res=0
    while x>0:
        t=x%10 # x의 1의자리
        res=res*10+t
        x=x//10
    return res

# 소수인지 아닌지 판별하는 함수
def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True

if __name__ == "__main__":
    뒤집은소수()