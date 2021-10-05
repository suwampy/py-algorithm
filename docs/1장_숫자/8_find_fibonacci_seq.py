import math
## 피보나치 수열
## 피보나치 수열 = 첫쨰 및 둘쨰 항이 1이며 그 이후의 모든 항은 바로 앞 두 항의 합인 수열

## 반복문
def find_finbonacci_seq_iter(n):
    if n < 2 :
        return n
    a, b = 0, 1
    for i in range(n) :
        a, b = b, a + b
    print('두번쨰')
    print(a)
    print(b)
    return a

##  재귀
def find_fibonacci_seq_rec(n):
    if n < 2 : return n
    return find_fibonacci_seq_rec(n-1) + find_fibonacci_seq_rec(n-2)

## 수식 사용
def find_fibonacci_seq_form(n):
    ## sqrt : 제곱근 반환
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    ## floor : 반올림
    return int(math.floor(phi ** n / sq5))

def test_find_fib():
    n=5
    find_fibonacci_seq_rec(n)
    find_finbonacci_seq_iter(n)
    find_fibonacci_seq_form(n)

if __name__ == "__main__":
    test_find_fib()